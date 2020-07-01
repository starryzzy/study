#-*- codeing = utf-8 -*-
#@Time : 2020/3/14 19:56
#@Author : zzy
#@File : demo3.py
#@Software : PyCharm
'''
tup1=()#创建空的元组
#tup2=(50,)
tup2=(50,60,70)
print(type(tup1))
print(type(tup2))
'''
'''
tup1=("abc","def",2000,2020,333,444,555,666)
print(tup1[1:5])
list_zzy=["zbc",123,456,333,444,555,666]
print(list_zzy[1:5])
'''
'''
#增，连接
tup1=(12,34,56)
tup2=("abc","zyz")
tup=tup1+tup2
print(tup)
'''
'''
#删
tup1=(12,34,56)
print(tup1)
del tup1  #删除了整个元组变量
print("删除后：")
print(tup1)
'''


'''
info={"name":"吴彦祖","age":"18"}#zidiandedingyi
print(info["name"])
print(info["age"])
#print(info["gender"])
#print(info.get("gender"))
print(info.get("age","20"))
print(info.get("gender","m"))
'''
'''
#增
info={"name":"吴彦祖","age":"18"}
newID=input("请输入新的学号：")
info["id"]=newID
print(info["id"])
'''
'''
#删  del   clear
info={"name":"吴彦祖","age":"18"}
print("删除前：%s"%info["name"])
del info["name"]
print("删除后：%s"%info["name"])
'''
'''
info={"name":"吴彦祖","age":"18"}
print("删除前：%s"%info)
del info
print("删除后：%s"%info)
'''
'''
info={"name":"吴彦祖","age":"18"}
print("清空前：%s"%info)
info.clear()
print("清空后：%s"%info)
'''
'''
info={"name":"吴彦祖","age":"18"}
info["age"]=20
print(info["age"])
'''
'''
info={"id":1,"name":"吴彦祖","age":"18"}
print(info.keys())
print(info.values())
print(info.items())

for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''
mylist=["a","b","c","d"]
for i,x in enumerate(mylist):
    print(i+1,x)