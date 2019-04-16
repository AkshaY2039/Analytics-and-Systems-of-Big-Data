import pandas as pd
import numpy as np
import csv

# Read csv file into a pandas dataframe
df = pd.read_csv("HealthIndicatorONE.csv")
print('\n\n------------------------------isnull------------------------------\n\n')
print(df.isnull())

print('\n\n------------------------------notnull------------------------------\n\n')
print(df.notnull())

print('\n\n------------------------------fillna------------------------------\n\n')
print(df.fillna(0))

print('\n\n------------------------------fill previous values------------------------------\n\n')
print(df.fillna(method='pad'))

print('\n\n------------------------------fill next values------------------------------\n\n')
print(df.fillna(method='bfill'))
