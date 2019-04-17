# Hash Apriori using Spark

from __future__ import division
from collections import namedtuple, Counter
from math import ceil
from itertools import combinations
from pyspark import SparkContext

global minSupport
global dsSize
global freqItems
global global_dataset

maximumItems = 0
minSupport = 15  # in percentage
minConfidence = 10 # in percentage
dsSize = 0

def readData (file):
	global dsSize
	global maximumItems
	items = set ()
	fd = open (file, 'r')
	x = list ()
	for itemset in fd:
		a=list (map (int, itemset.strip ().split (",")))
		con  = frozenset (a)
		items = items | con
		dsSize +=1
		x.append (a)
	maximumItems = len (items)
	return x

def nextFrequent (itemsets,dataset):
	global minSupport
	it = set ()
	for i in range (0,len (itemsets)-1):
		ilen = len (itemsets[i])
		for j in range (i+1,len (itemsets)):
			jlen=len (itemsets[j])
			if (set (itemsets[i][:ilen-1]) == set (itemsets[j][:jlen-1])):
				new_itemset = list (itemsets[i])
				new_itemset.append (itemsets[j][jlen-1])
				it.add (tuple (new_itemset))
	final_it = list ()
	for i in it:
		count =0
		for d in dataset:
			if set (i).issubset (set (d)):
				count+=1
		if count >= minSupport:
			final_it.append (i)
	return final_it

def nextFrequent_hash (itemsets,i1):
	global minSupport
	bucket_size = 17
	hashtable = [ [] for _ in range (0,bucket_size) ]
	frequent = list ()
	for i in itemsets:
		for j in range (0, len (str (i))-1):
			for k in range (j+1,len (i)):
				hash = (i[j]*10 + i[k])%bucket_size
				hashtable[hash].append ( (i[j],i[k]))
	print ("\n\n Hash Table:\n")
	for i in range (0,bucket_size):
		x = Counter (hashtable[i])
		print (x)
		for a in x.keys ():
			if x[a]>=minSupport:
				frequent.append (a)
	return frequent

def apriori (indices):
	global global_dataset
	print (indices)
	global freqItems
	dataset = global_dataset[indices[0]:indices[1]]
	items = list ()
	freq =list ()
	for i in range (2,maximumItems):
		if i<3:
			freq = nextFrequent_hash (dataset,i)
			print ("\n\nFreq = ", freq)
		else:
			freq = nextFrequent (freq,dataset)
			print ("\n\nFreq = ", freq)
		items = items + freq
		if len (freq)<=1:
			break
	print ("Items =", items)
	freqItems = freqItems + items
	# print ("\nFrequent Items: ")
	return items

if __name__ == "__main__":
	noOfPartition = 4
	global_dataset = readData ("./smoking_hours.csv")
	freqItems = list ()
	sc = SparkContext ("local", "apriori")
	minSupport = minSupport*dsSize/100
	size=0
	indices = list ()
	while size<dsSize:
		a = size
		b = size + dsSize/4
		b=int (ceil (b))
		if b>dsSize:
			b=dsSize
		size = b
		indices.append ( (a,b))
	print (indices)
	d = sc.parallelize (indices, 4)
	d.foreach (apriori)