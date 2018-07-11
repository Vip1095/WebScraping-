f = open('train2.csv')
f1 = open('train3.csv','w')
#a = []
for l in f :
	j = l.strip().split(',')
	m = j[5]

	if m == '1985' or m == '1987' :
		j[5] = '1'

	elif m == '1999' or m == '1998' :
		j[5] = '2'

	elif m == '1997' :
		j[5] = '2'	

	elif m == '2002' or m == '2004' :
		j[5] = '3'

	else :
		j[5] = '4'

	k = ','.join(j)
	f1.write(k+'\n')


#print list(set(a))