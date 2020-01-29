import datetime
import time

# 获取当前时间
dtime = datetime.datetime.now()
un_time = time.mktime(dtime.timetuple())
print(un_time)

# 将unix时间戳转换为“当前时间”格式
times = datetime.datetime.fromtimestamp(un_time)
print(times)