## load packages
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import pandas as pd
import scipy as sp
import numpy as np
import math
# from sklearn.impute import *
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

## load data
sim_dat = pd.read_csv('https://raw.githubusercontent.com/happyrabbit/DataScientistR/master/Data/SegData.csv')
sim_dat.head()
sim_dat.describe()

## find the position of bad values
bad_obs = sim_dat['age'] > 100
## replace the value with NaN
sim_dat.loc[bad_obs, 'age'] = np.NaN
## same for store_exp
bad_obs = sim_dat['store_exp'] < 0
sim_dat.loc[bad_obs, 'store_exp'] = np.NaN

## check if it is replaced successfully
sim_dat['age'].hasnans
sim_dat['store_exp'].hasnans


### Impute missing values with mean/median/mode

## If strategy='mean', then replace missing values using the mean along each column.
## Can only be used with numeric data.
imp_mean = SimpleImputer(missing_values=np.NaN, strategy='mean')
## get only the columns need to be filled
data_with_imputed_mean = imp_mean.fit_transform(sim_dat[['age', 'store_exp']])

## If strategy='median', then replace missing values using the median along each column.
## Can only be used with numeric data.
imp_median = SimpleImputer(missing_values=np.NaN, strategy='median')
## get only the columns need to be filled
data_with_imputed_median = imp_median.fit_transform(sim_dat[['age', 'store_exp']])

## If strategy='most_frequent', then replace missing using the most frequent value along each column.
## Can be used with strings or numeric data.
imp_mode = SimpleImputer(missing_values=np.NaN, strategy='most_frequent')
## get only the columns need to be filled
data_with_imputed_mode = imp_mode.fit_transform(sim_dat[['age', 'store_exp']])

## replace the columns
## don't run here since we will need to show other imputation methods later
## sim_dat[['age','store_exp']] = data_with_imputed_values

### K-nearest neighbors

sim.dat

imp<-preProcess(sim.dat,method="knnImpute",k=5)
# need to use predict() to get KNN result
demo_imp<-predict(imp,sim.dat)
