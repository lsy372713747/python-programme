#coding:utf-8
s1 = raw_input("请输入第一个数字： ")
s2 = raw_input("请输入第二个数字： ")
s3 = raw_input("请选择运算法则：0.+,1.-,2.*,3./:       ")
if s3.find("+") >-1:
    print s1,s2
    print int(s1) + int(s2)
if s3.find("-") >-1:
    print s1,s2
    print int(s1) - int(s2)
if s3.find("*") >-1:
    print s1,s2
    print int(s1) * int(s2)
if s3.find ("/")>-1:
    print s1,s2
    print int(s1) / int(s2)