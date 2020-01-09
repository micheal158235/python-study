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


print("-----------------代码块的表示----------------")
a = -100
if a >= 0:
    print("|a| =", a)
else:  #冒号代表后面缩进语句是代码块
    print("|a| =", -a)
