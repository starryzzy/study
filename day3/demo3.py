#-*- codeing = utf-8 -*-
#@Time : 2020/3/19 21:33
#@Author : zzy
#@File : demo3.py
#@Software : PyCharm
'''
try:
    print("-----test----1-----")
    f=open("123.txt","r")
    print("-----test----2-----")
except IOError:
    pass
'''
'''
try:
    print(num)
except NameError:
    print("产生错误")
'''
'''
try:
    print("-----test----1-----")
    f=open("test1.txt","r")
    print("-----test----2-----")
    print(num)
except Exception as result :
    print("产生错误")
    print(result)
'''
import time
try:
    f=open("test1.txt","r")
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常")
