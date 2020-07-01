#-*- codeing = utf-8 -*-
#@Time : 2020/3/19 21:13
#@Author : zzy
#@File : demo2.py
#@Software : PyCharm
'''
f=open("test.txt","w")
f.write("Hello world,i am here!")
f.close()
'''
'''
f=open("test.txt","r")
content=f.read(5)
print(content)
content=f.read(10)
print(content)
f.close()
'''
'''
f=open("test.txt","r")
content=f.readlines()
print(content)
i=1
for temp in content:
    print("%d:%s"%(i,temp))
    i+=1
f.close()
'''
'''
f=open("test.txt","r")
content=f.readline()
print("1:%s"%content,end="")
content=f.readline()
print("2:%s"%content)
f.close()
'''
import os
os.rename("test.txt","test1.txt")