import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# Read csv file into a pandas dataframe
# df = pd.read_csv("HealthIndicatorTWO.csv")

# print ("Data Loading Started")
# with open ('HealthIndicatorTWO.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print (row['State_Name'],'  ',row['AA_Sample_Units_Total'],'    ',row['AA_Sample_Units_Rural'],'    ',row['AA_Sample_Units_Urban'])

# df = pd.DataFrame(reader, columns = ['State_Name', 'AA_Sample_Units_Total', 'AA_Sample_Units_Rural', 'AA_Sample_Units_Urban'])


#Create a Dictionary of series
d = {'State_Name':pd.Series(['Assam','Bihar','Chhattisgarh','Jharkhand','MadhyaPradesh','Odisha','Rajasthan','UttarPradesh','Uttarakhand']),
   'AA_Sample_Units_Total':pd.Series([1784,2356,1255,2108,2557,2364,1841,3927,2501]),
   'AA_Sample_Units_Rural':pd.Series([1412,1981,926,1513,1660,1798,1294,2782,1962]),
   'AA_Sample_Units_Urban':pd.Series([372,375,329,595,897,566,547,1145,539])
}

#Create a DataFrame
df = pd.DataFrame(d)
print ('DataFrame')
print (df)
print ('\n')
#Sum
print ('Sum')
print (df.sum())
print ('\n')
#Mean
print ('Mean')
print (df.mean())
print ('\n')
#Std Deviation
print ('Standard Deviation')
print (df.std())
print ('\n')
#Minimum
print ('Min')
print (df.min())
print ('\n')
#Maximum
print ('Max')
print (df.max())
print ('\n')
#Description
print ('Describe')
print (df.describe())

plt.plot(df.describe())
plt.show()
