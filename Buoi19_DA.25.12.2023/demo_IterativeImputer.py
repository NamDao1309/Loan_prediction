import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge

csv_path = "Buoi19_DA.25.12.2023\horse-colic.csv"
# step 1 : read csv file
df = pd.read_csv(csv_path, header=None, na_values='?', skiprows=1)

# step 2:
data = df.values

# define object imputer
imputer = IterativeImputer(estimator=BayesianRidge(), imputation_order='descending')

# fit value on dataset
imputer.fit(data)

# transform the dataset
x_trans = imputer.transform(data)
print(x_trans)