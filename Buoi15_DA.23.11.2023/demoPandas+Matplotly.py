import pandas as pd
import csv

df = pd.read_csv("https://gist.githubusercontent.com/bobbyhadz/9061dd50a9c0d9628592b156326251ff/raw/381229ffc3a72c04066397c948cf386e10c98bee/employees.csv", nrows=3, usecols=(1,2))
print(df)

csv_path ="VIETECH_DA_28.09.2023//Buoi15_DA.23.11.2023//hocsinh.csv"
df1 = pd.read_csv(csv_path)
print(df1)

dta_path = "VIETECH_DA_28.09.2023//Buoi15_DA.23.11.2023//cars.dta"
df2 = pd.read_stata(dta_path)
print(df2)