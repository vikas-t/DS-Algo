import Tac
import os
import re
import glob
import time

nodeName = '00000000c72a4f4f-AWM-1'

class Downscale:
   def __init__(self,sensorName,minimusEntity,windowLength,expiration):
      self.minimusEntity = minimusEntity
      self.windowLength = windowLength
      self.expiration = expiration
      self.bucket = {}
      self.bucketMax = -1
      self.bucketMin = -1
      self.currentTime = time.time()
      self.sensorName = sensorName
      self.minTime = time.time()-self.windowLength
      print "Mintime: %f"%self.minTime
      self.count = 0

   def addEntry(self,ts,val):
      if ts<self.minTime:
         return

      self.count += 1
      self.mayBeFlush(ts)
      self.bucket[ts] = val
      if ts>self.bucketMax or self.bucketMax==-1:
         self.bucketMax = ts
      if ts<self.bucketMin or self.bucketMin==-1:
         self.bucketMin = ts

   def mayBeFlush(self,ts):
      if self.bucketMax-self.bucketMin>self.expiration:
         self.flush()
         return

      if self.bucketMin+self.expiration<ts:
         self.flush()
         return
      
      if self.bucketMax-self.expiration>ts:
         self.flush()
         return

   def flush(self):
      self.bucketMax = -1
      self.bucketMin = -1
      bucketLen = len(self.bucket)
      if bucketLen==0:
         return

      avg = sum(self.bucket.values())/bucketLen
      key = sorted(self.bucket.keys())[0]
      self.minimusEntity.floatVal[key] = avg
      print "   %s[%f] = %f"%(self.sensorName,key,avg)
      self.bucket.clear()


Tac.activityThread().start()
sysdbAddr = 'tbt:///Central'

localMountIntf = Tac.mountTop().defaultMountIntf()
localMountIntf.setPrefix(sysdbAddr)
localMountIntf.setLocalPrefixOverride("/")

localMountIntf.setTypeName("Tac::Dir")
localMountIntf.mount('Data/Logged/minimus','wtfi-a')
localMountIntf.completeSync()

assert(localMountIntf.mountErrors==0)
minimusTable = Tac.entity('Data/Logged/minimus')
monthlyTable = minimusTable['monthly']
weeklyTable = minimusTable['weekly']

csvFileList = glob.glob("*csv")

currentSensor = ""
skipSensor = ""

monthlyDownscale = None
weeklyDownscale = None

for fn in csvFileList:
   f = open(fn)
   f.readline()
   print "Loading %s"%fn
   for line in f:
      (ts,_,sensorName,value) = line.strip().split(',')
      if sensorName==skipSensor:
         continue
      if sensorName!=currentSensor:
         # Sensor changed
         if sensorName not in monthlyTable[nodeName]:
            print "   %s is not in monthly table"%sensorName
            skipSensor = sensorName
            continue
         if sensorName not in weeklyTable[nodeName]:
            print "   %s is not in weekly table"
            skipSensor = sensorName
            continue
         print "   Processing %s"%sensorName
         currentSensor = sensorName
         if monthlyDownscale:
            monthlyDownscale.flush()
            print "monthlyDownscale processed %d entries"%monthlyDownscale.count
         if weeklyDownscale:
            weeklyDownscale.flush()
            print "weeklyDownscale processed %d entries"%weeklyDownscale.count
         monthlyDownscale = Downscale(sensorName+"-m",monthlyTable[nodeName][sensorName],3600*24*30,3600*24*30/1000)
         weeklyDownscale = Downscale(sensorName+"-w",weeklyTable[nodeName][sensorName],3600*24*7,3600*24*7/1000)
      monthlyDownscale.addEntry(float(ts),float(value))
      weeklyDownscale.addEntry(float(ts),float(value))

   monthlyDownscale.flush()
   weeklyDownscale.flush()

   f.close()
