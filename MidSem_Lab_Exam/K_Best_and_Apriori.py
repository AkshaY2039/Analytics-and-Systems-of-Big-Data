from sklearn.feature_selection import SelectKBest, chi2
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def readMatrix(file):
	fd = open(file, 'r')
	x = list()
	y = list()
	for itemset in fd:
		a=list(itemset.strip().split(","))
		for i in range (1, len (a)):
			q = str (ord(a[i][0]))
			r = q + a[i][1]
			a[i] = int (r)
		# print (a)
		x.append(a[1:] )
		y.append(ord(a[0]))
	return x,y

def save_file(x,y):
	f = open("new_data.csv", "w")

	n = len(y)
	for i in range(0,n):
		a =list (map(str,list(x[i])))
		a.insert(0,str(y[i]))
		f.write(",".join(a))
		f.write("\n")

if __name__ =="__main__":
	X,y = readMatrix("./transformed.csv")
	print ("\nInitial no of columns: ",len(X[0]))
	print ("initial dataset row: \n",X[0])
	X_new = SelectKBest(chi2, k=10).fit_transform(X, y)
	print ("\nAfter processing: ",X_new.shape[1])
	print ("\n\n new dataset\n",X_new)
	# X_new = X_new.astype(int)
	# print (X_new[0])
	# np.savetxt("k_sig.csv", X_new, delimiter=",")

	save_file(X_new,y)

	te = TransactionEncoder()
	te_ary = te.fit(X_new).transform(X_new)
	df = pd.DataFrame(te_ary, columns=te.columns_)

	frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

	print ("\n --------------------------------------------------------------------------------------------------------------")
	print ("								 FREQUENT ITEMSETS GENERATED")
	print ("-----------------------------------------------------------------------------------------------------------------")
	print ("\n\n\n",frequent_itemsets)

	rules=association_rules(frequent_itemsets, metric="support", min_threshold=0.1)
	print ("\n --------------------------------------------------------------------------------------------------------------")
	print ("								 ASSOCIATION RULES GENERATED")
	print ("-----------------------------------------------------------------------------------------------------------------")
	print ("\n\n\n",rules)
