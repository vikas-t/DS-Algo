import pickle
import os
import glob
import re
import sys

timeFrom = 0
timeTo = 1506506148

dataDir = '/var/lib/Controller/storage/csvPrecache'
nodeName = '00000000c72a4f4f-AWM-1'
#sensorList = ['current0','current1','current2','current3','pressure0','pressure1','temperature2','temperature3','temperature4','temperature5']
sensorList = ['temperature2', 'temperature3', 'temperature4', 'temperature5', 'temperature6', 'temperature7', 'temperature8', 'temperature9', 'temperature10', 'temperature11', 'temperature-11-CompSuctionTemp','temperature-11-CompSuctionTemp_1','temperature12', 'temperature13', 'temperature14', 'temperature15']


def writeLine(fh,val):
   fh.write(val+"\n")


for sensorName in sensorList:
   outputFile = open(nodeName+"-"+sensorName+'.csv','w')
   writeLine(outputFile,"timestamp,nodename,sensorname,value")
   sensorData = {}
   filesPattern = os.path.join(dataDir,nodeName,sensorName,'21600_*')
   fileList = glob.glob(filesPattern)
   tsRe = re.compile('21600_([0-9]*)_python')
   entries = 0
   for fn in sorted(fileList):
      m = tsRe.search(fn)
      if not m:
         continue
      ts = int(m.group(1))*21600
      if (ts+21600)<=timeFrom or ts>timeTo:
         # Out of range
         continue

      with open(fn) as f:
         try:
            obj = pickle.load(f)
         except EOFError,e:
            print "   %s - EOFError %s"%(fn,str(e))
            continue
      sensorData.update(obj)
      entries += len(obj)
      for k in sorted(sensorData.keys()):
         writeLine(outputFile,"%.6f,%s,%s,%.7f"%(k,nodeName,sensorName,sensorData[k]))
      sensorData.clear()
   print "   %s - %d entries" % (sensorName,entries)

   print "Exported data for %s" % sensorName
   outputFile.close()
   print "Data written to %s"%(nodeName+"-"+sensorName+".csv"