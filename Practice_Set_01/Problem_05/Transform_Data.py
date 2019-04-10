def readMatrix (file):
	fd = open (file, 'r')
	x = list ()
	y = list ()
	f = open ('transformed.csv','w')
	fd.readline ()
	for itemset in fd:
		a = list (itemset.strip ().split (","))
		for i in range (1, len (a)):
			a[i] = a[i] + str(i)
		# print a
		# a= map (str,a)
		f.write (",".join (a))
		f.write ("\n")
		x.append (a[1:] )
		y.append (a[0])
	f.close ()
	fd.close ()

	return x,y


if __name__ =="__main__":
	readMatrix ("./agaricus-lepiota.csv")
