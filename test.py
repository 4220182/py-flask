'''
参考：https://realpython.com/list-comprehension-python/#using-conditional-logic
'''

def getval(a):
    return a * 3

a = {'a':1, 'b':2, 'c':3}
s = {k: getval(s) for k,s in a.items() if s>2}
print(s)

a = [1,2,3]
s = [k * 2 for k in a]
print(s)