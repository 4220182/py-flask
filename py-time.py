'''
参考：
https://www.runoob.com/python/python-date-time.html

格式化时间：
1. 分析日志中一段时间的记录，如分析日志中：2020-12-23 20:30:31 -- 2020-12-23 20:30:31 之间的日志。
'''

import time
from dateutil.parser import parse

'''
格式化时间
'''
'''
格式化时间戳为日期：
time.strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
语法：time.strftime(format[, t])
参数：
format -- 格式字符串。
t -- 可选的参数t是一个struct_time对象。
返回值：
返回以可读字符串表示的当地时间
'''
timestamp = 1596380702
print(time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(timestamp)))

'''
格式化字符串日期为时间戳
time.strptime(string[, format]): 根据指定的格式把一个时间字符串解析为时间元组。
参数:
string -- 时间字符串。
format -- 格式化字符串。
返回值:
返回struct_time对象

time.mktime(t): 返回用秒数来表示时间的浮点数。
参数:
t -- 结构化的时间或者完整的9位元组元素。
返回值: 
返回用秒数来表示时间的浮点数。

'''
a = "2020 05 07 22:24:24"
print(time.mktime(time.strptime(a,"%Y %m %d %H:%M:%S")))

'''
时间相减
'''
a = "2020 05 07 22:24:24"
b = "2020 05 08 22:24:24"
start = time.mktime(time.strptime(a, "%Y %m %d %H:%M:%S"))
end = time.mktime(time.strptime(b, "%Y %m %d %H:%M:%S"))
print(time.strptime(a, "%Y %m %d %H:%M:%S"))
print("bt-at, value:", (end-start)/60/60/24, "天")

'''
使用dateutil工具，处理时间相减
'''
a = parse('2017-10-01/12:12:12.343')
b = parse('2013-3-4/10:10:10.134')
print(a, (a-b).days)
print((a-b).seconds)
print((a-b).total_seconds())