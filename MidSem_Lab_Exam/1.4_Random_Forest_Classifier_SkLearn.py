#	Random Forest Classifier - SciKit Learn

import numpy
import csv
from sklearn.ensemble import RandomForestClassifier

dataAttributes = []
dataClass = []

Attributes = {
	"0": {},	# ediblity:					edible=e,poisonous=p
	"1": {},	# cap-shape:				bell=b,conical=c,convex=x,flat=f,knobbed=k,sunken=s
	"2": {},	# cap-surface:				fibrous=f,grooves=g,scaly=y,smooth=s
	"3": {},	# cap-color:				brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
	"4": {},	# bruises?:					bruises=t,no=f
	"5": {},	# odor:						almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
	"6": {},	# gill-attachment:			attached=a,descending=d,free=f,notched=n
	"7": {},	# gill-spacing:				close=c,crowded=w,distant=d
	"8": {},	# gill-size:				broad=b,narrow=n
	"9": {},	# gill-color:				black=k,brown=n,buff=b,chocolate=h,gray=g,green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
	"10": {},	# stalk-shape:				enlarging=e,tapering=t
	"11": {},	# stalk-root:				bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?
	"12": {},	# stalk-surface-above-ring:	fibrous=f,scaly=y,silky=k,smooth=s
	"13": {},	# stalk-surface-below-ring:	fibrous=f,scaly=y,silky=k,smooth=s
	"14": {},	# stalk-color-above-ring:	brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
	"15": {},	# stalk-color-below-ring:	brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
	"16": {},	# veil-type:				partial=p,universal=u
	"17": {},	# veil-color:				brown=n,orange=o,white=w,yellow=y
	"18": {},	# ring-number:				none=n,one=o,two=t
	"19": {},	# ring-type:				cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z
	"20": {},	# spore-print-color:		black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y
	"21": {},	# population:				abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y
	"22": {},	# habitat:					grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d
}

classNames = {}

entityIndex = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,0]
attributesIndex = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
classIndex = 0

# Loading Data
print ("Data Loading Started"), 
with open ('./agaricus-lepiota.csv') as csvdata: 
	readCSV = csv.reader (csvdata, delimiter=',')
	next (readCSV)	# Skipping Header content
	for row in readCSV: 
		for i in entityIndex: 
			if (row[i] in Attributes[str (i)]) == False: 
				Attributes[str (i)][row[i]] = len (Attributes[str (i)].keys())
				if (i == classIndex): 
					classNames[row[i]] = 0
		datarow = []
		try: 
			for i in attributesIndex: 
				datarow.append (Attributes[str (i)][row[i]])
			dataAttributes.append (datarow)
			dataClass.append (Attributes[str (classIndex)][row[classIndex]])
		except ValueError: 
			pass
feats = [	"cap-shape",
			"cap-surface",
			"cap-color",
			"bruises?",
			"odor",
			"gill-attachment",
			"gill-spacing",
			"gill-size",
			"gill-color",
			"stalk-shape",
			"stalk-root",
			"stalk-surface-above-ring",
			"stalk-surface-below-ring",
			"stalk-color-above-ring",
			"stalk-color-below-ring",
			"veil-type",
			"veil-color",
			"ring-number",
			"ring-type",
			"spore-print-color",
			"population",
			"habitat"]

print ("Features: ", feats)
print ("Class Labels: ", list (classNames.keys ()))

print ("Done Loading Data")

# seperating test and training data
testDataAttributes = numpy.asarray (dataAttributes [3000:])
checkDataClass = numpy.asarray (dataClass[3000:])
dataAttributes = numpy.asarray (dataAttributes[:3000])
dataClass = numpy.asarray (dataClass[:3000])

#training classifier
print ("\n\nClassifier training Started")
rFClf = RandomForestClassifier(n_estimators=2, random_state=1)
rFClf.fit (dataAttributes, dataClass)
print ("Classifier training Finished")

predClass = rFClf.predict(testDataAttributes)

# measuring classifier accuracy
totalPoints = float (testDataAttributes.shape[0])
mislabeled = float ((checkDataClass == predClass).sum())
print ("Number of mislabeled points out of total %d points : %d" % (totalPoints, mislabeled))
print ("Classifier Model Accuracy: ", (1 - (mislabeled / totalPoints)) * 100.0)

# checking with random record
randomIndex = 1251
print ("\n\nClassifying testDataAttributes [", randomIndex, "]")
record = testDataAttributes[randomIndex]
print (record)
record = record.reshape (1, -1)
classPredSingle = rFClf.predict (record)
print ("Predicted Class Label: ")
print (classPredSingle)
print ("Actual Class Label : ")
print (checkDataClass[randomIndex])