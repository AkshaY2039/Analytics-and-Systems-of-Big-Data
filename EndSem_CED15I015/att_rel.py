import csv

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules
import numpy as np

# csv file name
filename = "HealthIndicatorTWO.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename) as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
temp=rows
frow=["0"] * 9
l=[]
for i in range(0,len(rows)):
    for j in range(1,4):
        rows[i][j]=rows[i][j].replace('\n', ' ')
        l.append(rows[i][j].split(" "))

dataset=l
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
print (frequent_itemsets)
x=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
print (x)
