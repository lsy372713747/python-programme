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
