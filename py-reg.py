'''
r'^A\\[(.*)\\]$'
#此句中 r 表示去掉反斜杠的转移机制
'''
import re

line = "a[book1,test5,1005, book6,test6,1006, book7,test7,1007, book8,test8,1008]"

s = '^A\\[(.*)\\]$'
pattern = re.compile(s, re.I)
match = re.match(pattern, line)
if match :
    print(match.group(1))

pattern = "^A\\[(.*)\\]$"
match = re.match(pattern, line, re.I)
if match :
    print(match.group(1))

line = "a\[book1,test5,1005, book6,test6,1006, book7,test7,1007, book8,test8,1008]"

s = r'^A\[(.*)]$'
pattern = re.compile(s, re.I)
match = re.match(pattern, line)
if match :
    print("test:",match.group(1))


line = "book1,test5,1005, book6,test6,1006, book7,test7,1007, book8,test8,1008"
pattern =",\d+"
s = re.sub(pattern, ",ABC", line)
print("re.sub: ", s)

# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('number'))
    return str(value * 2)

line = "book1,test,1005, book6,test6,1006, book7,test7,1007, book8,test8,1008"
pattern ="(?P<number>\d+)"
s = re.sub(pattern, double, line)
print("end: ", s)
