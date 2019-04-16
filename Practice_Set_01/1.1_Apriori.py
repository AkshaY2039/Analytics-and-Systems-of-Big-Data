#	Apriori Algorithm for Association Rule Mining
#		Batch No. 08 - CED15I015, CED15I019, CED15I031

import numpy
import csv
from apyori import apriori

txnDataMale = []
txnDataFemale = []

# Loading Data
print ("Data Loading Started"), 
with open ('../DataSets/daily_smoking_times.csv') as csvdata: 
	readCSV = csv.reader (csvdata, delimiter=',')
	next (readCSV)	# Skipping Header content
	for row in readCSV: 
		try: 
			if (row[0] == 'M'): 
				values = row[2:7]
				txnDataMale.append (numpy.asarray (values))
			else: 
				values = row[2:7]
				txnDataFemale.append (numpy.asarray (values))
		except ValueError: 
			pass
print ("Done Loading Data\n")

txnDataMale = numpy.asarray (txnDataMale[:1000])

a_rules_male = list (apriori (txnDataMale, min_support = 0.01, min_confidence = 0.02, min_lift = 2, min_length = 4))

for m_item in a_rules_male: 
	pair = m_item[0]
	m_items = [x for x in pair]
	print ("Rule : " + m_items[0] + " --> " + m_items[1] + "\t\tSupport : " + (str (m_item[1]))[0:6] + "\tConfidence : " + (str (m_item[2][0][2]))[0:6] + "\tLift : " + (str (m_item[2][0][2]))[0:7])

print ("*************Finished Here with Male Data************\n")

txnDataFemale = numpy.asarray (txnDataFemale[:1000])

a_rules_female = list (apriori (txnDataFemale, min_support = 0.01, min_confidence = 0.02, min_lift = 2, max_length = None))

for f_item in a_rules_female: 
	pair = f_item[0]
	f_items = [x for x in pair]
	print ("Rule : " + f_items[0] + " --> " + f_items[1] + "\t\tSupport : " + (str (f_item[1]))[0:6] + "\tConfidence : " + (str (f_item[2][0][2]))[0:6] + "\tLift : " + (str (m_item[2][0][2]))[0:7])

print ("*************Finished Here with Female Data************\n")