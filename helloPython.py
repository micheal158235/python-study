#教学参考网址：https://www.liaoxuefeng.com/wiki/1016959663602400
#python版本：python3.8

#以下第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，在源代码中写的中文输出可能会有乱码。
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("--------------测试'''代替\\n-----------------")
#print(r'测试'''') 语法报错
#print(r'测试\'''') 输出 “测试\'”
print(r'测试\'\'\'')
print('测试\'\'\'')
print("测试'''")
print('line11\nline12\nline13')
print('''line21
line22
line23''')
print('''"2<3:"
2 < 3
"2>3:"
2 > 3''')

print("--------------测试字符串引用-----------------")
print ("please enter: I'm \"Ok\"", '"', '""', "''", \
       '\'',"\"",'\\\n\\',r'\\\n\\') #\\表示的字符就是\; \n表示换行; r''表示''内部的字符串默认不转义


print("---------测试各种数值类型的输入方式----------")
#注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，
#      例如Java对32位整数的范围限制在-2147483648-2147483647。
#      Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
name = input()
print ("hello world!",name)
print("0x400 * 0x300 =", 0x400*0x300)
print("1024 * 768 =", 1024*768)
print("1.024e3 * 7680e-1+1 =", 1.024e3*7680e-1+1) #1.024e3=1024; 7680e-1=768
print("10//3=", 10//3)#地板除，结果只有整数，没有小数
print("10/3=", 10/3)
print("9/3=", 9/3)#就算能整除，得到的结果也是符点数
print("10%3=", 10%3)

print("input_s是字符串，请输入整数(小数不也行)，否则报错")
input_s = input('birth:')
birth = int(input_s)
if birth < 2000:
    print('00前')
else:
    print('00后')

PI = 3.14159265359
print("常量一般建议全大写：PI=", PI);


print("-------------------布尔数据------------------")
print(True,False,"\n2<3:",2 < 3,"\n2>3:",2 > 3)
print("2<3 and 2>3:", 2 < 3 and 2 > 3)
print("2<3 or 2>3:", 2 < 3 or 2 > 3)
print("not 2<3:", not 2<3)
print("None != 0:", None)

print("-----------------字符串的编码----------------")
print("在最新的Python 3版本中，字符串以Unicode编码")
print("ord('A')=", ord('A')) #获取字符的Unicode整数表示
print("ord('中')=", ord('中'))
print("chr(66)=", chr(66)) #把Unicode编码转换为对应的字符
print("chr(25991)=", chr(25991))
print("'\u4e2d\u6587'", '\u4e2d\u6587')#如果知道字符的整数编码，还可以用十六进制这么写str

#Python对bytes类型(1个字节)的数据用带b前缀的单引号或双引号表示
#要注意区分'ABC'（占6个字节）和b'ABC'（占3个字节），前者是str，
#后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
encode_x = b'ABC'
print("ABC ascii 表现形式:",'ABC'.encode('ascii'))#Unicode转ascii 输出:b'ABC'
print("中文 utf-8 bytes表现形式:",'中文'.encode('utf-8')) #Unicode转utf-8， 输出:b'\xe4\xb8\xad\xe6\x96\x87'
#print('中文'.encode('ascii')) 出错：因为中文编码的范围超过了ASCII编码的范围
print("b'\xe4\xb8\xad\xe6\x96\x87'=",b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))#utf-8编码中0xe4b8ad:中 0xe69687:文  输出:中文
print("b'\xe4\xb8\xad\xff':", b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节

print("'ABC'占多少个Unicode字符:",len('ABC'))
print("'中文'占多少个Unicode字符:",len('中文'))
print("utf-8编码的'ABC'占多少个字节", len(b'ABC'))
print("utf-8编码的'ABC'占多少个字节", len(b'\xe4\xb8\xad\xe6\x96\x87'))
print("utf-8编码的'ABC'占多少个字节", len('中文'.encode('utf-8')))

print("-----------------格式化输出------------------")
print('格式化方式和C语言是一致的')
print('Hello, %s' % 'world')#如果只有一个%?，括号可以省略
print('Hi, %s, you have $%d' %('Micheal', 10000))
print('Age:%s Gender:%s float:%.2f' % (25, True, 3.1415926))#如果不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('growth rate:%d%%' % 7)#有些时候，字符串里面的%是一个普通字符,这个时候就需要转义，用%%来表示一个%
print('Hello, {0}, 成绩提升了 {1:.2f}'.format('小明', 17.125))#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多

print("-----------------list内容可变-----------------")
classmates = ['Micheal', 'Bob', 'Tracy']
list_empty = []
print("classmates=%s len(classmates)=%d list_empty=%s" %(classmates, len(classmates), list_empty))
print("classmates[0]=%s, classmates[1]=%s, classmates[2]=%s, classmates[3]越界 \nclassmates[-1]=%s, classmates[-2]=%s, classmates[-3]=%s, classmates[-4]越界"
      %(classmates[0], classmates[1], classmates[2],classmates[-1], classmates[-2], classmates[-3]))

print("classmates.pop(1)=", classmates.pop(1), "classmates=", classmates)
print("classmates.pop()=", classmates.pop(), "classmates=", classmates)
#print("classmates.pop(1)后classmates=%s" %(classmates.pop(1), classmates))   %(classmates.pop(1))报错
#print("classmates.pop()=%s, classmates=%s" %(classmates.pop(), classmates))  %(classmates.pop(1))报错

#classmates[1] = 123            由于classmates= ['Micheal']只有一个元素了，classmates[1]赋值越界
#classmates[2] = ['asp', 'php'] 由于classmates= ['Micheal']只有一个元素了，classmates[2]赋值越界
#clsssmates[3] = True           由于classmates= ['Micheal']只有一个元素了，classmates[3]赋值越界
classmates.insert(1, 123)
classmates.insert(2, ['asp', 'php'])
classmates.insert(3, True)
classmates.insert(6, False)
classmates.append('Jack')
print("classmates=%s len(classmates)=%d classmates[2][1]=%s" %(classmates, len(classmates), classmates[2][1]))

print("空list[]的长度=" , len([]))
#print("空list[]的长度=" % len([]))         报错
#print("空list[]的长度=" % len(list_empty)) 报错

print("----------------tuple内容不可变----------------")
print("list的pop(),insert(1,'Tom'),append(123),list[1]=2\n在tuple中全部不能用，因为tuple中的元素指向是不可用的")
classmates = ('Micheal', 'Bob', 'Tracy')
tuple_empty = ()
print("classmates=%s, tuple_empty=%s" %(classmates, tuple_empty))
print("tuple中只有一个元素表示法:t=(1)不是tuple, t(1,)才是tuple")

t=('a', 'b', ['A', 'B'])
print("t=%s", t)
#t[2,0] = 'X'  此种写法报错
#t[2,1] = 'Y'  此种写法报错
t[2][0] = 'X'
t[2][1] = 'Y'
print("tuple的每个元素，指向永远不变,但是指向中的内容可变")
print("t=%s", t)


print("------------------代码块的表示-----------------")
a = 0
if a >= 0:#冒号代表后面缩进语句是代码块
    print("a>=0")
    print("|a| =", a)
elif a == 0:
    print("|a| =", a)
else:  
    print("|a| =", -a)

print("----------------------循环---------------------")
names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print(name)
print("range(5)=%s list(range(5))=%s" %(range(5), list(range(5))))
sum = 0
for x in range(101):
    sum = sum + x
    print("sum_temp=", sum)
print("sum=", sum)

n = 1
while n <= 100:
    if n >10:
        break
    print("n=", n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print('END')


print("---------------------dict字典-------------------")
d = {'Micheal':95, 'Bob':75, 'Tracy':85}
print("dict=", d)

#print("Thomas", d['Thomas'])  等于Thomas的key不存在，dict报错
#调用之前最好判断一下
if 'Thomas' in d:
    ("Thomas", d['Thomas'])
#通过dict提供的get()方法也可以获取value，如果key不存在，可以返回None，或者自己指定的value
print("d.get('Thomas')=%s  d.get('Thomas',-1)=%s" %(d.get('Thomas'),d.get('Thomas',-1)))

d.pop('Bob')
print("after d.pop('Bob') dict=", d)

print('在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key')
key = [1, 2, 3]
#d[key] = 'a list'  报错


print("-----------------------set----------------------")
s = set([1, 2, 3])
print("set([1, 2, 3])=", s)
s = set([1, 1, 2, 2, 3])
print("set([1, 1, 2, 2, 3])=", s)
s.add(4)
print("s.add(4)后s=", s)
s.remove(4)
print("s.remove(4)后s=", s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print("set([1,2,3]) & set([2,3,4]) =", s1 & s2)
print("set([1,2,3]) | set([2,3,4]) =", s1 | s2)







    
