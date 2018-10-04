import time
import datetime
ticks=time.time()
print("no of ticks since 1 jan 1970",ticks)
print(time.localtime())
localtime = time.localtime(time.time())
print ("Local current time :", localtime)
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
d=datetime.date(2019,8,20)
print(d)

