f = open('train.csv')
f1 = open('train1.csv','w')
for i in f :
	j = i.strip().split(',')
	if j[1] == 'Low Fat' or j[1] == 'low fat' : 
		j[1] = '1'
	elif j[1] == 'LF' :
		j[1] = '1'
	elif j[1] == 'reg' or j[1] == 'Regular' :
		j[1] = '2'

	if j[3] == 'Seafood' : 
		j[3] = '1'
	elif j[3] == 'Frozen Foods' :
		j[3] = '2' 
	elif j[3] == 'Health and Hygiene' :
		j[3] = '3'
	elif j[3] == 'Meat' :
		j[3] = '4'
	elif j[3] == 'Starchy Foods' :
		j[3] = '5'
	elif j[3] == 'Canned' :
		j[3] = '6'
	elif j[3] == 'Household' :
		j[3] = '7'
	elif j[3] == 'Snack Foods' :
		j[3] = '8'
	elif j[3] == 'Hard Drinks' :
		j[3] = '9'
	elif j[3] == 'Dairy' :
		j[3] = '10'
	elif j[3] == 'Baking Goods' :
		j[3] = '11'
	elif j[3] == 'Soft Drinks' :
		j[3] = '12'
	elif j[3] == 'Breads' :
		j[3] = '13'
	elif j[3] == 'Breakfast' :
		j[3] = '14'
	elif j[3] == 'Fruits and Vegetables' :
		j[3] = '15'
	else :
		j[3] = '16'
 
 	if j[6] == 'Small' :
		j[6] = '1'
	elif j[6] == 'High' :
		j[6] = '3'
	else :
		j[6] = '2'

	if j[7] == 'Tier 1' :
		j[7] = '1'
	elif j[7] == 'Tier 3' :
		j[7] = '3'
	else :
		j[7] = '2'

	if j[8] == 'Supermarket Type1' :
		j[8] = '1'
	elif j[8] == 'Supermarket Type2' :
		j[8] = '2'
	elif j[8] == 'Supermarket Type3' :
		j[8] = '3'
	else :
		j[8] = '4'

	k = ','.join(j)
	f1.write(k+'\n')