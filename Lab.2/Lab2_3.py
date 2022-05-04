# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 00:27:51 2022

@author: Administrator
"""


from random import *
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import math
from decimal import Decimal
from decimal import getcontext
import numpy as np

# 班级人数从10到50变化，班级数从1000到10000变化，查看P的变化
n= 10 #每个班级的人数
flag = 0
mlist = []
plist1 = []
for m in range(1000,10001,100):
    flag =0
    mlist.append(m)
    for i in range(0,m):
        birthday = [randint(1, 366) for j in range(n)]
        set_birthsay = set(birthday)
        if len(birthday)!=len(set_birthsay):
            flag+=1
    plist1.append(flag/m)

data1 = DataFrame(plist1, index = mlist, columns=['10'])

n= 20 #每个班级的人数
flag = 0
mlist = []
plist1 = []
for m in range(1000,10001,100):
    flag =0
    mlist.append(m)
    for i in range(0,m):
        birthday = [randint(1, 366) for j in range(n)]
        set_birthsay = set(birthday)
        if len(birthday)!=len(set_birthsay):
            flag+=1
    plist1.append(flag/m)
data1['20'] = plist1

n= 30 #每个班级的人数
flag = 0
mlist = []
plist1 = []
for m in range(1000,10001,100):
    flag =0
    mlist.append(m)
    for i in range(0,m):
        birthday = [randint(1, 366) for j in range(n)]
        set_birthsay = set(birthday)
        if len(birthday)!=len(set_birthsay):
            flag+=1
    plist1.append(flag/m)
data1['30'] = plist1

n= 40 #每个班级的人数
flag = 0
mlist = []
plist1 = []
for m in range(1000,10001,100):
    flag =0
    mlist.append(m)
    for i in range(0,m):
        birthday = [randint(1, 366) for j in range(n)]
        set_birthsay = set(birthday)
        if len(birthday)!=len(set_birthsay):
            flag+=1
    plist1.append(flag/m)
data1['40'] = plist1

n= 50 #每个班级的人数
flag = 0
mlist = []
plist1 = []
for m in range(1000,10001,100):
    flag =0
    mlist.append(m)
    for i in range(0,m):
        birthday = [randint(1, 366) for j in range(n)]
        set_birthsay = set(birthday)
        if len(birthday)!=len(set_birthsay):
            flag+=1
    plist1.append(flag/m)
data1['50'] = plist1

print(data1)
plt.figure(figsize=(10, 3))
plt.plot(data1)
plt.xlabel('Amount of Classes')
plt.ylabel('Proportion')
plt.legend(labels = ['10','20','30','40','50'])
plt.show()

#在M=1000的情况下，班级人数从1到365变化，查看P的变化
m = 1000 #班级数固定
flag = 0
nlist = []
plist1 = []
for n in range(1,366):
    nlist.append(n)
    flag =0
    for i in range(m):
        birthday = [randint(1, 366) for j in range(n)]
        set_birthsay = set(birthday)
        if len(birthday)!=len(set_birthsay):
            flag+=1
    plist1.append(flag/m)

plt.figure(figsize=(10,3))
plt.plot(nlist,plist1,color='r')
plt.annotate('(22,0.492)', xy=(21,0.492), xytext=(40,0.492),arrowprops=dict(arrowstyle='->'))
plt.xlabel("Each Class Persons")
plt.ylabel('Proportion')
plt.show()

#用理论上的生日相同函数求生日相同概率，查看和实际求出来的概率之间的拟合程度
n2 = np.arange(1,366)
p2 = []
for i in n2:
    value = Decimal(math.factorial(365)//math.factorial(365-i))
    for j in range(0,i):
        value = Decimal(value/365)
    value = 1-value
    p2.append(value)

plt.figure(figsize=(10, 3))
plt.plot(nlist,plist1,color='r',label='Real')
plt.plot(n2,p2,color='b',label='Theoretical')
plt.legend()
plt.xlabel("Each Class Persons")
plt.ylabel('Proportion')
plt.show()
