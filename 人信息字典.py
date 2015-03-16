import random
lk = []
for x in xrange(0,1000000):
	k = random.randint(1000000,10000000)
	lk.append(k)
print len(lk)
k = random.sample(lk,100000)
xin = dict()
for x in k:
	name = "jeapedu" + str(x)
	year = random.randint(1990,1999)
	if x % 5 == 1:
		race = "meng"
	else:
		race = "han"
	if x % 3 == 1:
		 sex = "nv"
	else:
		sex = "nan"
	v = [name,year,race,sex]
	xin.setdefault(x,v)
#1dk = xin.keys()
c = 0
s = 0
#1for x in dk:
for x in k:
	if 1995 == xin[x][1]:
		c += 1
		print "name==>",xin[x][0]
		if xin[x][3] == "nv":
			s += 1
print c,c*1.0/100000,s*1.0/c

