rs = '''aa bb ct uu dd yy fg 
tt yy ww mm cc bx hh
ss dd zz bx
li mm bc gg
tx cx bx qq
pp cx gg nn ee'''
b = []
e = []
x = []
d = []
bn = "bb"
en = "ee"
def roadInfo(s):
	dinfo = []
	rlist = s.split("\n")
	i = 0
	for x in rlist:
		print 'r' + str(i),x.split()
		dinfo.append(x.split())
		i += 1
	return dinfo
#d = []
#d = roadInfo(rs)
#print 'd',d
def findExchange(r1,r2):
	li = []
	for x in r1:
		if x in r2:
			temp = x,r1.index(x),r2.index(r2)
			li.append(temp)
	if len(li) == 0:
		return [(-1,-1,-1)]
	return li
print 'get all roads info'
print 'find all begin end exchange'
def diffStation(allroad,be):
	i = 0
	for dr in d:
		px = findExchange(dr,[bn,en])
		print 'px',px
		for p in px:
			if p[0] == "bb":
				b.append(i)
			elif p[0] == "ee":
				e.append(i)
			else:
				c.append(i)
		i += 1
	print b,e,c
diffStation(d,[bn,en])