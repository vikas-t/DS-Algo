#!/usr/bin/python

# https://www.hiredintech.com/classrooms/algorithm-design/lesson/19/task/16


def sort_the_files(n, result):
   
   def printr(s, e, result):
      cnt = len(result)
      for i in xrange(s, e):
         if cnt <= 1000:
            result.append(i)
            cnt = cnt + 1
         else:
             return False
      return True


   m = 1
   for i in xrange(1,10):
      mr = True
      while mr:
         if i*m < n:
            lr = i*m
         else:
            mr = False
            break

         if (i+1)*m < n:
            hr = (i+1)*m
         else:
            hr = n+1
         
         if printr(lr, hr, result):
            m = m * 10
         else:
            mr = False
            break
   
   return result
   
   
print sort_the_files(113, [])

