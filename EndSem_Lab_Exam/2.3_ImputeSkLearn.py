# Impute values using Sk Learn

import numpy as np
from pandas import read_csv
from sklearn.impute import SimpleImputer

imp = SimpleImputer (missing_values=np.nan, strategy='mean')
dataset = read_csv('./HealthIndicatorONE.csv', header=0)
imp.fit(dataset[["YY_Infant_Mortality_Rate_Imr_Urban_Person"]].head(15))

print ("\nData with NaN / NA")
print(dataset[["YY_Infant_Mortality_Rate_Imr_Urban_Person"]].head(15))

print ("\nData After Imputing Mean")
print(imp.transform(dataset[["YY_Infant_Mortality_Rate_Imr_Urban_Person"]].head(15)))