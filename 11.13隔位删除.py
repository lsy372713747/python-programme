#coding:utf-8
#约瑟夫抽杀问题
l1 = range(1,101)
def del_list(l2):
    temp = []
    for i in range(1,len(l2)+1):
        if i % 3 != 0:
            temp.append(l2[i-1])

    remain = i % 3 
    if remain:
        del temp[-remain:]
        return l2[-remain:] + temp
    else:
        return temp
while len(l1) > 2:
    print l1
    x = del_list(l1) 
    l1 = x
    raw_input("continue:")
print l1

  


'''
l1 = range(1,101)
y = 0
def del_list(l2,offset):
    temp = []
    for i in range(1,len(l2)+1):
        if (i+offset) % 3 != 0:
            temp.append(l2[i-1])
    remain = (i+offset) % 3
    return temp,remain
while len(l1) > 2:
    x,y = del_list(l1,y)
    print x,y
    l1 = x
'''
'''
count = 2
while 1:
    if count > len(l1)-1:
        break
    else:
        print l1[count]
        count +=3
'''
'''
a_list=[]
for a in l1-1:
    a_list.append(a.remove("a"))
    print a_list
'''
