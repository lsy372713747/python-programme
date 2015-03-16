#coding:utf-8
import random

l1 = ["石头","剪刀","布"]
c = random.randint(0,2)

res=[
"石头"+"石头",2,
"石头"+"剪刀",1,
"石头"+"布",0,
"剪刀"+"石头",1,
"剪刀"+"布",0,
"剪刀"+"剪刀",2,
"布"+"剪刀",0,
"布"+"布",2,
"布"+"石头",1
]

win=["电脑赢","你赢了","平"]

p = raw_input("请输入0.石头,1.剪刀,2.布:     ")
c1 = res[res.index(l1[int(p)] + l1[c]) +1]
print win[c1]

import time
time.sleep(5)


