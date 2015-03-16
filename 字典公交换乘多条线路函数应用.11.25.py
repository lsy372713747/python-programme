#coding:utf-8
r1 = "aa bb cx uu dd yy gg"
r2 = "yy mm ww xx cc bx hh"
r3 = "er ct ym mm zz ee"
bn = "bb"
en = "ee"
rd1 = r1.split()
rd2 = r2.split()
rd3 = r3.split()
d = []
d.append(rd1)
d.append(rd2)
d.append(rd3)
print rd1
print rd2
print rd3
def findexchange(r1,r2):
	li = []
	for x in r1:
		if x in r2:
			temp = x,r1.index(x),r2.index(x)
			li.append(temp)
	return li
'''
print "-----------------"
findexchange(rd1,rd2)
findexchange(rd1,rd3)
findexchange(rd2,rd3)
findexchange(rd1,[bn,en])
findexchange(rd2,[bn,en])
findexchange(rd3,[bn,en])
print "-----------------"
'''
i = 0
b = []
e = []
for dr in d:
	px = findexchange(dr,[bn,en])
#	print 'px->',px,px[0],px[0][0]
	for p in px:
		if p[0] == "bb":
			b.append(i)
		if p[0] == "ee":
			e.append(i)
	i += 1
print 'b,e',b,e
print "--------------"
for begin in b:
	for end in e:
		print begin,end,
		ret = findexchange(d[begin],d[end])
#		print ret
		if len(ret) == 1:
			print 'need exchange once',
			print ret
		if len(ret) == 0:
			print 'twice exchange'
			print 'ret',ret
			ret1 = findexchange(d[begin],d[3 - begin - end])
			ret2 = findexchange(d[end],d[3 - begin - end])
			print begin,3 - begin - end,ret1
			print end,3 - begin - end,ret2