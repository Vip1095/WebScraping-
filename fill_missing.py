f = open('train1.csv')
f2 = open('train2.csv','w')
# print "TRAIN\n"
# l1 = [] ; l3 = [] ; l6 = [] ; l7 = [] ; l8 = []
a = []
for i in f :
	
	j = i.strip().split(',')
	try :
		a.append(float(j[0]))
	except :
		pass
	# for k in range(len(j)) :
	# 	if j[k] == '' :

b = sorted(a)
c = int(len(a)/2)			
d = b[c]

f = open('train1.csv')
for l in f :	
	j = l.strip().split(',')
	print j
	if j[0] == '' :
		j[0] = str(d)
	k = ','.join(j)
	f2.write(k+"\n")




# 	l1.append(j[1]) ; l3.append(j[3]) ; l6.append(j[6]) ; l7.append(j[7]) ; l8.append(j[8])

# print list(set(l1)),'\n'
# print list(set(l3)),'\n'
# print list(set(l6)),'\n'
# print list(set(l7)),'\n'
# print list(set(l8)),'\n'
