# Drop missing values using Pandas

from pandas import read_csv
import numpy

dataset = read_csv('./HealthIndicatorONE.csv', header=0)
# # mark zero values as missing or NaN
# dataset = dataset.replace(0, numpy.NaN)

print (dataset.head(40).dropna(axis = 1))
# # drop rows with missing values
# dataset.dropna(inplace=True)
# # summarize the number of rows and columns in the dataset
# print(dataset.shape)