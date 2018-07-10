'''
基本类型：
string
int
float
boolean
'''

count = 0
"""
num = 1
while num <= 100:
    count += num
    num += 1
"""
for i in range(1,101):
    count += i
print('count 1 to 100, result is', count, sep=":")


a = True
b = not a
print('a is', a)
print('b is', b)

print("He said, \"I\'m yours!\"")
print("\\\\_v_//")
print("Stay hungry, \nstay foolish.\n      -- Steve Jobs")

for i in range (0,5) :
    
    if i<=2:
        j = 1 + i*2
    else:
        j = -2*i + 9
    for k in range(1, j+1):
        print("*", end='')
    print("")

"""
print("How old are you?")
age = input()
print("Oh, you are " + age)
myAge = 2
print("my age is " + str(myAge))
print("you are older than me, " + str(eval(age) - myAge))
"""

"""
int(x) #把x转换成整数
float(x) #把x转换成浮点数
str(x) #把x转换成字符串
bool(x) #把x转换成bool值
"""
a = 1
print(a)
a = float(a) + 0.5
print(a)
a = str(a) + "567"
print(a)
a = "True"
a = not bool(a)
print(a)

"""
在python中，其他类型转成 bool 类型时，以下数值会被认为是False：
   为0的数字，包括0，0.0
   空字符串，包括''，""
   表示空值的None
   空集合，包括()，[]，{}
其他的值都认为是True。
"""
print("bool(-123):", bool(-123))
print("bool(0)", bool(0))
print("bool('abc')", bool('abc'))
print("bool('False')", bool('False'))
print("bool('')", bool(''))
print("bool(' ')", bool(' '))

def sayHello():
    print('hello world!')
sayHello()

def sayHello2(name):
    print(str(name),',hello world!')
sayHello2("XiaoKa")
sayHello2(123)

print(list(range(1, 11)))

l = [365, 'everyday', 0.618, True]
for i in l:
    print(i)

"""
slice, 似乎就是subList？
切片操作符是在[]内提供一对可选数字，用:分割。冒号前的数表示切片的开始位置，冒号后的数字表示切片到哪里结束。同样，计数从0开始。
注意，开始位置包含在切片中，而结束位置不包括。
l[1:3]
"""
for i in l[1:3]:
    print(i)

'''
def lifecycle(lifeNum):
    print(lifeNum)
    lifeNum += 1
    print(lifeNum)
print("===============")
life = 1
lifecycle(life)
lifecycle(life)
lifecycle(life)
lifecycle(life)
lifecycle(life)
print(life)
'''

section = 'Hi. I am the one. Bye.'

'''print(list(section.split(".")))'''


s = ';'
li = ['apple', 'pear', 'orange']
fruit = s.join(li)
print(fruit)

print(''.join(['hello', 'world']))


word = 'helloworld'
for c in word:
   print(c)

print(word[0])
print(word[-2])

print(word[1:8])
print(word[:5])
print(word[5:])
print(word[:])

newword = ','.join(word)
print(newword)


f = open(r'C:\Users\RanWeizheng\Desktop\pyTest\db-connect-info.txt')
'''
data = f.read()
print(data)
'''
print("readline")
print(f.readline())
print(f.readline())
print("readlines")
fList = f.readlines()
for str in fList:
    print("readlines:",str)
f.close()

"""

out.write('a string you want to write')
out.close()



lines = f.readlines()
f.close()
print(lines)

result = '%s\t:%d\n'%('abc', 67)
print(result)
"""
'''
print(list(range(10)))
for i in range(10):
    a = input()
    if a == 'EOF':
        break
'''

# 0 1 0 1 0 |1|2
'''
i = 0
while i < 5:
   i += 1
   for j in range(3):
       print(j)
       if j == 2:
           break
   for k in range(3):
       if k == 2:
           continue
       print(k)
   if i > 3:
       break
   print(i)
'''

print()
print()

try:
   f = open('non-exist.txt')
   print('File opened!')
   f.close()
except:
   print('File not exists.')
print('Done')


score = {
   '萧峰': 95,
   '段誉': 97,
   '虚竹': 89
}
print(score['段誉'])
print(score.get('段誉'))
print(score.get('慕容复'))

score['虚竹'] = 91
score['慕容复'] = 59
del score['段誉']
for name in score:
   print(name, '：', score[name])

dict = {}

'''
import random
from math import pi
print(pi)
'''
from math import pi as math_pi
print(math_pi)

# python3 标准库
# http://www.runoob.com/python3/python3-stdlib.html



def helloDefault(name='world'):
    print('hello', name)
helloDefault()
helloDefault('XiaoKa')
