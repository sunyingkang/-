#date类
from datetime import datetime

a = datetime.today()
print(a)
print(a.year)  #输出年
print(a.month) #输出月
print(a.day)   #输出日


from datetime import date

a=date.today()
print(a)
print(a.year)
print(a.month)
print(a.day)
a=date(2017,3,1)
b=date(2017,3,15)
print(a.__eq__(b))
print(a.__ge__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__lt__(b))
print(a.__ne__(b))
print(a.__sub__(b))
print(a.__rsub__(b))

print(a.__format__('%y-%m-%b'))
print(a.__format__('%y/%m/%b'))
print(a.__format__('%D'))
print(a.__format__('%d'))




#time类
from datetime import time
a=time(12,20,30,899)

print(a)
print(a.__format__('%H:%M:%S'))



from datetime import  *
dt = datetime(2012,12,12,23,59,59)
print(dt)

#昨天
dt1=dt+timedelta(days=-1)
print(dt1)
#明天
dt2=dt+timedelta(days=1)
print(dt2)
#上一个小时
dt3=dt+timedelta(hours=-1)
print(dt3)
#下一个小时
dt4=dt+timedelta(hours=1)
print(dt4)

#time 模块
import time

a = time.time()
for x in range(100000):
    pass
b=time.time()-a
print(b)
#第一次调用，返回程序实际的运行时间
print(time.perf_counter())
#第二次调用，返回的是距离上一次调用的时间隔
print(time.perf_counter())
#第三次调用，
print(time.perf_counter())
#如果没有给定时间戳，直接返回当前时点的国际伦敦时间
print(time.gmtime())
#可以将时间戳转变为本地时间
print(time.localtime())
a =time .time()
#如果没有给定时间戳，直接返回当前时点的本地时间
time.localtime(a)

print("start:%s" %time.ctime())
time.sleep(5)
print("End:%s" %time.ctime())

print(time.time())

print(time.ctime(time.time()))
#将时间元组转化为farmat年月日格式
a=time.strftime("%Y-%m-%d %X",time.gmtime())
print(a)

b=time.strftime("%y-%m-%d %X")
print(b)
#返回当地的日期和时间
c=time.strftime("%x %x")
print(c)

#calendar模块
import calendar
thismonth=calendar.month(2021,11,0)
print(thismonth)

#2018年为平年 所以为False
print(calendar.isleap(2018)) #False
#2008年为如年，所以为True
print(calendar.isleap(2008)) #True





