#-*- codeing = utf-8 -*-
#@Time : 2020/3/8 21:47
#@Author : zzy
#@File : demo2.py
#@Software : PyCharm

#namelist=[]
namelist=["小张","小王","小李"]
'''
testlist=[1,"测试"]
print(namelist[0])
print(type(testlist[1]))
'''
'''
for name in namelist:
    print(name)

lenth=len(namelist)
i=0
while i<lenth:
    print(namelist[i])
    i+=1
'''
'''
print("----增加前名单列表的数据----")
for name in namelist:
    print(name)
nametemp=input("请输入添加学生的姓名：")
namelist.append(nametemp)

print("----增加后名单列表的数据----")
for name in namelist:
    print(name)
'''
'''
a=[1,2]
b=[3,4]
a.append(b)
print(a)

a.extend(b)
print(a)
'''

'''
a=[0,1,2]
a.insert(1,3)
print(a)

'''
'''
movieName=["加勒比海盗","骇客帝国","第一滴血","指环王","速度与激情"]
print("----删除前电影列表的数据----")
for name in movieName:
    print(name)

#del movieName[2]
#movieName.pop()
movieName.remove("指环王")
print("----删除后电影列表的数据----")
for name in movieName:
    print(name)
'''
'''

print("----增加前名单列表的数据----")
for name in namelist:
    print(name)

namelist[1]="小红"

print("----增加后名单列表的数据----")
for name in namelist:
    print(name)
'''

'''
findName=input("请输入你要查找的学生姓名：")
if findName in namelist:
    print("zhaodao")
else:
    print("meoizhaod")
'''



mylist=["a","b","c","a","b"]

'''
print(mylist.index("a",1,4))
print(mylist.index("a",1,3))

print(mylist.count("c"))


a=[1,4,2,3]
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)


#schoolNames=[[],[],[]]
schoolNames=[["北京大学","清华大学"],["南开大学","天津大学","天津师范大学"],["山东大学","中国海洋大学"]]
print(schoolNames[0][0])

import random
offices=[[],[],[]]
names=["A","B","C","D","E"]
for name in names:
    index=random.randint(0,2)
    offices[index].append(name)
i=1
for office in offices:
    print("办公室的%d人数为：%d"%(i,len(office)))
    i+=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)
    
'''
'''
products=[["iphone",6888],["Macpro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
print("------ 商品列表 ------")
i = 0
for shang in products:

    print(i,end="\t")
    i += 1
    for pin in shang:
        print(pin,end="\t")
    print(" ")
'''
'''
products=[["iphone",6888],["Macpro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
gouwuche=[]
print("以下是我们的一个商品列表：")
i = 0
for shang in products:

    print("你想买这件商品吗？",i,end="\t")
    i += 1
    for pin in shang:
        print(pin,end="\t")
    print(" ")
num=input("请输入你想买的商品的编号：")
for n in num:
    gouwuche.append(products[n])
tuichu=input("请输入q退出:")
j = 0
for s in gouwuche:

    print(j ,end="\t")
    j += 1
    for p in s:
        print(p,end="\t")
    print(" ")
    
'''





list_order=[]
while True:
    name=input("请输入您要购买的商品：（输入q退出）")
    if name=="q":
        break
    else:
        count=int(input("请输入您要购买的数量："))
        list_order.append([name,count])
for itme in list_order:
    print("您购买了：%s,买了%d件"%(itme[0],itme[1]))
