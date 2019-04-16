# Fill NA Forward or Backward

from pandas import read_csv
import numpy

dataset = read_csv('./HealthIndicatorONE.csv', header=0)
# # mark zero values as missing or NaN
# dataset = dataset.replace(0, numpy.NaN)

print ("\nData with NaN / NA")
print (dataset[["YY_Infant_Mortality_Rate_Imr_Urban_Person"]].head(10))
print ("\nData after Forward Fill / Padding")
print (dataset[["YY_Infant_Mortality_Rate_Imr_Urban_Person"]].head(10).fillna(method='pad'))
print ("\nData after Backward Fill")
print (dataset[["YY_Infant_Mortality_Rate_Imr_Urban_Person"]].head(10).fillna(method='bfill'))