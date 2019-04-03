#	Voting Classifier - SciKit Learn

import numpy
import csv
from sklearn.naive_bayes import ComplementNB
from sklearn import neighbors
import graphviz
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier

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

n_neighbors = 50

# seperating test and training data
# testDataAttributes = numpy.asarray (dataAttributes [3000:])
# checkDataClass = numpy.asarray (dataClass[3000:])
# dataAttributes = numpy.asarray (dataAttributes[:3000])
# dataClass = numpy.asarray (dataClass[:3000])

cNBClf = ComplementNB ()

dTreeClf = tree.DecisionTreeClassifier()

gNBClf = GaussianNB()

nNClf = neighbors.KNeighborsClassifier (n_neighbors, weights = 'distance')

lRCLf = LogisticRegression(solver='liblinear')

rFClf = RandomForestClassifier(n_estimators=2, random_state=1)

vClf = VotingClassifier(estimators=[('cnb', cNBClf), ('dt', dTreeClf), ('nn', nNClf), ('lr', lRCLf), ('rf', rFClf), ('gnb', gNBClf)], voting='hard')

for clf, label in zip([cNBClf, dTreeClf, nNClf, lRCLf, rFClf, gNBClf, vClf], ['Complement Naive Bayes', 'Decision Tree', 'Nearest Neighbors', 'Logistic Regression', 'Random Forest', 'Gaussian Naive Bayes', 'Ensemble/Voting']):
	scores = cross_val_score(clf, dataAttributes, dataClass, cv=5, scoring='recall')
	# scoring can accept 'accuracy', 'average_precision', 'balanced_accuracy', 'f1', 'recall' etc
	# check these at https://scikit-learn.org/stable/modules/model_evaluation.html
	print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))

