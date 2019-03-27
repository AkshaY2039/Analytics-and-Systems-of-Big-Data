#	Nearest Neighbors Classifier - SciKit Learn

import numpy
import csv
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors

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

# taking only 2 attributes as to plot on the graph easily
entityIndex = [20,22,0]
attributesIndex = [20,22]
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
feats = [	# "cap-shape",
			# "cap-surface",
			# "cap-color",
			# "bruises?",
			# "odor",
			# "gill-attachment",
			# "gill-spacing",
			# "gill-size",
			# "gill-color",
			# "stalk-shape",
			# "stalk-root",
			# "stalk-surface-above-ring",
			# "stalk-surface-below-ring",
			# "stalk-color-above-ring",
			# "stalk-color-below-ring",
			# "veil-type",
			# "veil-color",
			# "ring-number",
			# "ring-type",
			"spore-print-color",
			# "population",
			"habitat"]

print ("Features: ", feats)
print ("Class Labels: ", list (classNames.keys ()))

print ("Done Loading Data\n")

n_neighbors = 50

h = 1  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#AAFFAA', '#FFAAAA'])
cmap_bold = ListedColormap(['#00FF00', '#FF0000'])

# seperating test and training data
testDataAttributes = numpy.asarray (dataAttributes [2500:])
checkDataClass = numpy.asarray (dataClass[2500:])
dataAttributes = numpy.asarray (dataAttributes[:2500])
dataClass = numpy.asarray (dataClass[:2500])

for weights in ['uniform', 'distance']:
	#training classifier
	print ("Classifier training Started for %s " % (weights))
	nNClf = neighbors.KNeighborsClassifier (n_neighbors, weights = weights)
	nNClf.fit (dataAttributes, dataClass)
	print ("Classifier training Finished for %s \n" % (weights))

	# Plot the decision boundary. For that, we will assign a color to each
	# point in the mesh [x_min, x_max]x[y_min, y_max].
	x_min, x_max = testDataAttributes[:, 0].min() - 1, testDataAttributes[:, 0].max() + 1
	y_min, y_max = testDataAttributes[:, 1].min() - 1, testDataAttributes[:, 1].max() + 1
	xx, yy = numpy.meshgrid(numpy.arange(x_min, x_max, h),
						 numpy.arange(y_min, y_max, h))
	Z = nNClf.predict(numpy.c_[xx.ravel(), yy.ravel()])
	print (Z)

	# measuring classifier accuracy
	# totalPoints = float (testDataAttributes.shape[0])
	# mislabeled = float (0)
	# for index in [0,len(testDataAttributes)]:
	# 	if (checkDataClass[index] == nNClf.predict([testDataAttributes[index]])):
	# 		mislabeled +=1

	# print ("Number of mislabeled points out of total %d points : %d" % (totalPoints, mislabeled))
	# print ("Classifier Model Accuracy: ", (1 - (mislabeled / totalPoints)) * 100.0)

	# Put the result into a color plot
	Z = Z.reshape(xx.shape)
	plt.figure()
	plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

	# Plot also the training points
	plt.scatter(dataAttributes[:, 0], dataAttributes[:, 1], c=dataClass, cmap=cmap_bold,
				edgecolor='k', s=20)
	plt.xlim(xx.min(), xx.max())
	plt.ylim(yy.min(), yy.max())
	plt.title("2-Class classification (k = %i, weights = '%s')"
			  % (n_neighbors, weights))

plt.show()