#-*- codeing = utf-8 -*-
#@Time : 2020/3/19 20:12
#@Author : zzy
#@File : demo1.py
#@Software : PyCharm
'''
def printinfo():
    print("--------------")
    print("人生苦短，我用Python")
    print("--------------")
printinfo()
printinfo()

'''
'''
def add2Num(a,b):
    c=a+b
    print(c)
add2Num(11,22)
'''
'''
d2Num(a,b):
    return a+b
result=add2Num(11,22)
print(result)
'''

'''
def divid(a,b):
    shang=a//b
    yushu=a%b
    return shang,yushu
sh,yu=divid(5,2)
print("商：%d，余数：%d"%(sh,yu))
'''
'''
def heng():
    print("----------")
heng()
def heng2():
    d=int(input("请输入打印店行数："))
    i=0
    while i < d:
        heng()
        i+=1
heng2()
'''

'''
def add3Num(a,b,c):
    return a+b+c
print(add3Num(1,2,3))
def aum3(a,b,c):
    d=add3Num(a,b,c)
    e=d/3
    print(e)
aum3(5,5,6)

'''
'''
def test1():
    a=300
    print("test1------修改前：a=%d"%a)
    a=100
    print("test1------修改hou：a=%d" % a)
def test2():
    a=500
    print("test1------：a=%d" % a)
test1()
test2()
'''
'''
a=100
def test1():
    global a
    print("test1------修改前：a=%d"%a)
    a=200
    print("test1------修改hou：a=%d" % a)
def test2():

    print("test1------：a=%d" % a)
test1()
test2()
'''