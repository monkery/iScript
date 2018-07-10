#47 OO (1)
s = 'how are you'
l = s.split()
print(dir(s))
print(dir(l))

#48 OO (2)
class MyClass:
    name="Sam"
    def sayHello(self):
        print("hello %s"%self.name)
        
mc = MyClass()
print(mc)
print(mc.name)
mc.sayHello()
mc.name = "Lily"
mc.sayHello()


#49 OO (3)
'''
class Car:
    speed = 0
    def drive(self, distance):
        time = distance / self.speed
        print(time)

car = Car()
car.speed = 60.0
car.drive(100.0)
car.drive(200)

car2 = Car()
car2.speed = 100
car2.drive(100)
car2.drive(200)
'''

#50 OO (4)

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print('need %f hour(s)' % (distance / self.speed))

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel
    def drive(self, distance):
        Vehicle.drive(self, distance)
        print('need %f fuels' % (distance * self.fuel))

b = Bike(15.0)
c = Car(80.0, 0.012)
b.drive(100.0)
c.drive(100.0)

#50 and-or技巧  
# 1 类似于 boolean?A:B  但又不一样
# 是通过 Python的 逻辑运算实现的
# 主要技巧点在 如何让A的值永远为真 c = (True and [a] or [b])[0]


#51 元组 tuple
'''
print '%s is %d years old' % ('Mike', 23)
('Mike', 23)就是一个元组。这是元组最常见的用处。
'''

def get_pos(n):
    return (n/2, n*2)
x, y = get_pos(50)
print(x)
print(y)

pos = get_pos(50)
print(pos[0])
print(pos[1])

#52 数学运算
'''
python的数学运算模块叫做math，再用之前，你需要
import math
math包里有两个常量：
math.pi
圆周率π：3.141592...
math.e
自然常数：2.718281...

数值运算：
math.ceil(x)
对x向上取整，比如x=1.2，返回2.0（py3返回2）

math.floor(x)
对x向下取整，比如x=1.2，返回1.0（py3返回1）

math.pow(x,y)
指数运算，得到x的y次方

math.log(x)
对数，默认基底为e。可以使用第二个参数，来改变对数的基底。比如math.log(100, 10)

math.sqrt(x)
平方根

math.fabs(x)
绝对值

三角函数: 
math.sin(x)
math.cos(x)
math.tan(x)
math.asin(x)
math.acos(x)
math.atan(x)
注意：这里的x是以弧度为单位，所以计算角度的话，需要先换算

角度和弧度互换: 
math.degrees(x)
弧度转角度
math.radians(x)
角度转弧度

以上是你平常可能会用到的函数。除此之外，还有一些，这里就不罗列，可以去
http://docs.python.org/2/library/math.html
查看官方的完整文档。

有了这些函数，可以更方便的实现程序中的计算。比如中学时代算了无数次的
(-b±√(b²-4ac))/2a
现在你就可以写一个函数，输入一元二次方程的a、b、c系数，直接给你数值解。好，这题就留作课后作业吧。
'''

#52 真值表



import re
tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))
print(re.findall(r'(\w)*oo(\w)',tt))#()表示子表达式 
#执行结果如下：
#['good', 'cool']
#[('g', 'd'), ('c', 'l')]


import re
text = "Hi, I am Shirley Hilton. I am his wife."
m = re.findall(r"Hi", text)
if m:
    print(m)
else:
    print('not match')


#60 random
import random
'''
random.randint(a, b)可以生成一个a到b间的随机整数，包括a和b。
random.random() 生成一个0到1之间的随机浮点数，包括0但不包括1，也就是[0.0, 1.0)。
random.uniform(a, b) 生成a、b之间的随机浮点数。不过与randint不同的是，a、b无需是整数，也不用考虑大小。
random.choice(seq)从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串。
random.randrange(start, stop, step)生成一个从start到stop（不包括stop），间隔为step的一个随机数。start、stop、step都要为整数，且start<stop。
random.sample(population, k)从population序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列。
random.shuffle(x)把序列x中的元素顺序打乱。shuffle直接改变原有的序列。
random.seed(x)来指定seed。
'''
print(random.choice([1, 2, 3, 5, 8, 13])) #list
print(random.choice('abc'))#string
print(random.choice(['hello', 'world'])) #字符串组成的list
print(random.choice((1, 2, 3))) #元组

print(random.randrange(1, 9, 2)) # 1 3 5 7中选一个
arr = [1, 2, 3, 5, 8, 13]
print(arr) 
random.shuffle(arr)
print(arr) 

#61 计时
'''
time.time()
time.sleep(secs)  sleep 单位为秒
'''

print("="*40)
import time
print(time.time())

starttime = time.time()
print('start:%f' % starttime)
for i in range(10):
    print(i)
endtime = time.time()  
print('end:%f' % endtime)
print('total time:%f' % (endtime-starttime) )


# 62 Debug
# /摊手 ，没啥说的

# where is 66？ 上面么。。。额 

# 64 Python Shell
# 同上

# 65 pickle & cPickle(用法相同，效率更高) 序列化用

import pickle
test_data = ['Save me!', 123.456, True]
f = open('test.data', 'wb')
pickle.dump(test_data, f, True)
f.close()

f2 = open('test.data', 'rb')
test_data = pickle.load(f2)
f2.close()
print(test_data)

'''
如果你想保存多个对象，一种方法是把这些对象先全部放在一个序列中，在对这个序列进行存储：
a = 123
b = "hello"
c = 0.618
data = (a, b, c)
...
pickle.dump(data, f)

另一种方法就是依次保存和提取：
pickle.dump(a, f)
pickle.dump(b, f)
pickle.dump(c, f)
...
x = pickle.load(f)
y = pickle.load(f)
z = pickle.load(f)

dump 方法可以增加一个可选的参数，来指定用二进制来存储：
pickle.dump(data, f, True)
而 load 方法会自动检测数据是二进制还是文本格式，无需手动指定。
【特别说明】python3中，通过pickle对数据进行存储时，必须用二进制(b)模式读写文件。
open(file_name, 'rb')
'''



# 66 列表解析 List Comprehension 
# 列表解析（也有翻译成列表综合），就是通过一个已有的列表生成一个新的列表。
list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = [i for i in list_1 if i % 2 == 0]
print(list_2)
list_3 = [i/2 for i in list_1 if i%2 == 0]
print(list_3)

#用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，以分号（;）分隔的形式输出。
list_test = [str(i) for i in range(1,101) if i%2==0 or i%3==0 or i%5==0]
print(list_test)
result = ';'.join(list_test)
print(result)
print(';'.join([str(i) for i in range(1,101) if i%2==0 and i%3==0 and i%5==0]))


# 67-69 函数的参数传递
'''
def func(a=1,b=2,c=3)
def calcSum(*args) 在变量前加上星号前缀（*），调用时的参数会存储在一个 tuple（元组）对象中，赋值给形参。在函数内部，需要对参数进行处理时，只要对这个 tuple 类型的形参（这里是 args）进行操作就可以了。因此，函数在定义时并不需要指明参数个数，就可以处理任意参数个数的情况。
func(**kargs) 把参数以键值对字典的形式传入。

可以混用
def func(x, y=5, *a, **b):
但是需要注意规则

在混合使用时，首先要注意函数的写法，必须遵守：
带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
元组参数(*args)须在带有默认值的形参(arg=)之后；
字典参数(**kargs)须在元组参数(*args)之后。
可以省略某种类型的参数，但仍需保证此顺序规则。

调用时也需要遵守：
指定参数名称的参数要在无指定参数名称的参数之后；
不可以重复传递，即按顺序提供某参数之后，又指定名称传递。

而在函数被调用时，参数的传递过程为：
1.按顺序把无指定参数的实参赋值给形参；
2.把指定参数名称(arg=v)的实参赋值给对应的形参；
3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
4.将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。
'''


#70 Lambda表达式 λ

'''
lambda 表达可以被看做是一种匿名函数。它可以让你快速定义一个极度简单的单行函数。譬如这样一个实现三个数相加的函数：
def sum(a, b, c):
    return a + b + c

等价于：
sum = lambda a, b, c: a + b + 

它的写法比 def 更加简洁。但是，它的主体只能是一个表达式，不可以是代码块，甚至不能是命令（print 不能用在 lambda 表达式中）。所以 lambda 表达式能表达的逻辑很有限。

def fn(x):
return lambda y: x + y
a = fn(2)
print a(3)
输出：
5
这里，fn 函数的返回值是一个 lambda 表达式，也就等于是一个函数对象。当以参数2来调用 fn 时，得到的结果就是：
lambda y: 2 + y

a = fn(2) 就相当于：
a = lambda y: 2 + y

所以 a(3) 的结果就是5。

lambda 表达式其实只是一种编码风格，这种写法更加 pythonic。这并不意味着你一定要使用它。事实上，任何可以使用 lambda 表达式的地方，都可以通过普通的 def 函数定义来替代。在一些需要重复使用同一函数的地方，def 可以避免重复定义函数。况且 def 函数更加通用，某些情况可以带来更好地代码可读性。
而对于像 filter、sort 这种需要内嵌函数的方法，lambda 表达式就会显得比较合适。这个我以后会再单独介绍。
'''
def fn(x):
    return lambda y: x + y
a = fn(2)
print(a(3))



#71 变量的作用域
def func(x):
    print('X in the beginning of func(x): ', x)
    x = 2
    print('X in the end of func(x): ', x)

x = 50
func(x)
print('X after calling func(x): ', x)

'''
当函数内部定义了一个变量，无论是作为函数的形参，或是另外定义的变量，它都只在这个函数的内部起作用。函数外即使有和它名称相同的变量，也没有什么关联。这个函数体就是这个变量的作用域。像这样在函数内部定义的变量被称为“局部变量”。
要注意的是，作用域是从变量被定义的位置开始。像这样的写法是有问题的：

改变传入值的方法：
一种方法是，用 return 把改变后的变量值作为函数返回值传递出来，赋值给对应的变量。比如开始的那个例子，可以在函数结尾加上
return x
然后把调用改为
x = func(x)

还有一种方法，就是使用“全局变量”。
在 Python 的函数定义中，可以给变量名前加上 global 关键字，这样其作用域就不再局限在函数块中，而是全局的作用域。
'''

def func2():
	global x
	print('X in the beginning of func(x): ', x)
	x = 2
	print('X in the end of func(x): ', x)
x = 50
func2()
print('X after calling func(x): ', x)

'''
前面讲的局部变量和全局变量是 Python 中函数作用域最基本的情况。实际上，还有一些略复杂的情况，比如：

程序可以正常运行。虽然没有指明 global，函数内部还是使用到了外部定义的变量。然而一旦加上
x = 2
这句，程序就会报错。因为这时候，x 成为一个局部变量，它的作用域从定义处开始，到函数体末尾结束。
建议在写代码的过程中，显式地通过 global 来使用全局变量，避免在函数中直接使用外部变量。
'''
def func3():
    print('X in the beginning of func(x): ', x)
    # x = 2
    print('X in the end of func(x): ', x)
x = 50
func3()
print('X after calling func(x): ', x)


#map 函数

lst_1 = [1,2,3,4,5,6]
def double_func(x):
    return x * 2
lst_2 = map(double_func, lst_1)
print(lst_2)
print(type(lst_2))



lst_1 = [1,2,3,4,5,6]

lst_2 = [1,3,5,7,9,11]

lst_3 = map(lambda x, y: x + y, lst_1, lst_2)

print(lst_3)


lst_1 = [1,2,3,4,5,6]

lst_2 = [1,3,5,7,9,11]

lst_3 = map(None, lst_1)

print(lst_3)

lst_4 = map(None, lst_1, lst_2)

print(lst_4)



'''
age = 50
while True:
    user_input_age = int(input("age is :"))
    if user_input_age == age:
        print("yes")
        break
    elif user_input_age > age:
        print("you guess smaller...")
    else :
        print("you guess biggst...")
'''


'''

import os

import urllib.request

base_dir = 'd:/spider/Maldives/'
imgUrl = 'http://imgsrc.baidu.com/forum/w%3D580/sign=08b3a1fd00d79123e0e0947c9d355917/64d97bcb0a46f21f7c3aafa6fa246b600d33aec9.jpg'
 
def mkdir(path):
	folder = os.path.exists(path)
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...%s  ---"%path)
		print("---  OK  ---")
	else:
		print("---  There is this folder!  ---")

mkdir(base_dir)
urllib.request.urlretrieve(imgUrl,'%s/%s.jpg'% (base_dir,'test'))
'''


#73 reduce
#reduce(function, iterable[, initializer])
#第一个参数是作用在序列上的方法，第二个参数是被作用的序列，这与 map 一致。另外有一个可选参数，是初始值。
#function 需要是一个接收2个参数，并有返回值的函数。它会从序列 iterable 里从左到右依次取出元素，进行计算。每次计算的结果，会作为下次计算的第一个参数。
#提供初始值 initializer 时，它会作为第一次计算的第一个参数。否则，就先计算序列中的前两个值。
from functools import reduce 
lst = range(1, 6)
def add(x, y):
	return x + y
print(reduce(add, lst))
#((((1+2)+3)+4)+5)

#同样，可以用 lambda 函数：
print(reduce((lambda x, y: x + y), range(1, 101)))




#74 多线程

很多人使用 python 编写“爬虫”程序，抓取网上的数据。



举个例子，通过豆瓣的 API 抓取 30 部影片的信息：



import urllib, time



time_start = time.time()

data = []

for i in range(30):

    print 'request movie:', i

    id = 1764796 + i

    url = 'https://api.douban.com/v2/movie/subject/%d' % id

    d = urllib.urlopen(url).read()

    data.append(d)

    print i, time.time() - time_start



print 'data:', len(data)



参考输出结果：

> python test.py

request movie: 0

0 0.741228103638

request movie: 1

1 1.96586918831

...

request movie: 28

28 12.0225770473

request movie: 29

29 12.4063940048

data: 30



程序里用了 time.time() 来计算抓取花费的时间。运行一遍，大约需要十几秒（根据网络情况会有差异）。



如果我们想用这套代码抓取几万部电影，就算中间不出什么状况，估计也得花上好几个小时。



然而想一下，我们抓一部电影信息的过程是独立，并不依赖于其他电影的结果。因此没必要排好队一部一部地按顺序来。那么有没有什么办法可以同时抓取好几部电影？



答案就是：多线程。



来说一种简单的多线程方法：



python 里有一个 thread 模块，其中提供了一个函数：



start_new_thread(function, args[, kwargs])



function 是开发者定义的线程函数，

args 是传递给线程函数的参数，必须是tuple类型，

kwargs 是可选参数。



调用 start_new_thread 之后，会创建一个新的线程，来执行 function 函数。而代码原本的主线程将继续往下执行，不再等待 function 的返回。通常情况，线程在 function 执行完毕后结束。



改写一下前面的代码，将抓取的部分放在一个函数中：



import urllib, time, thread



def get_content(i):

    id = 1764796 + i

    url = 'https://api.douban.com/v2/movie/subject/%d' % id

    d = urllib.urlopen(url).read()

    data.append(d)

    print i, time.time() - time_start

    print 'data:', len(data)



time_start = time.time()

data = []

for i in range(30):

    print 'request movie:', i

    thread.start_new_thread(get_content, (i,))



raw_input('press ENTER to exit...\n')



参考输出结果：

> python test.py

request movie: 0

request movie: 1

...

request movie: 28

request movie: 29

press ENTER to exit...

1 0.39500784874

data: 1

9 0.428859949112

data: 2

...

data: 28

21 1.03756284714

data: 29

8 2.66121602058

data: 30



因为主线程不在等待函数返回结果，所以在代码最后，增加了 raw_input，避免程序提前退出。



从输出结果可以看出：

在程序刚开始运行时，已经发送所有请求

收到的请求并不是按发送顺序，先收到就先显示

总共用时两秒多

data 里同样记录了所有30条结果



所以，对于这种耗时长，但又独立的任务，使用多线程可以大大提高运行效率。但在代码层面，可能额外需要做一些处理，保证结果正确。如上例中，如果需要电影信息按 id 排列，就要另行排序。



多线程通常会用在网络收发数据、文件读写、用户交互等待之类的操作上，以避免程序阻塞，提升用户体验或提高执行效率。



多线程的实现方法不止这一种。另外多线程也会带来一些单线程程序中不会出现的问题。这里只是简单地开个头。














































