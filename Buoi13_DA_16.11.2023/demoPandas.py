import pandas as pd
import numpy as np

# SERIES
# x = pd.Series([23, 45, 1, 55, 78])
# print(x)
# print(x.values)
# print(type(x.values))

# print(x[0])

# a = [1, 6, 9, 7]
# y = pd.Series(a, index=["x", "y", "z", "t"])
# print(y)
# print(y["x"])

# fruits = {1: "mango", 2:"banana", 3:"tomato", 4:"kiwi"}
# my_fruits = pd.Series(fruits)
# print(my_fruits)

# my_fruits2 = pd.Series()
# my_fruits2 = pd.Series(fruits, index=[0, 1, 2, 3,4])
# print(my_fruits2)

# # slicing
# print(my_fruits[2])
# print(my_fruits[0:3])

#DATAFRAME

table = {
    'id': [1, 2, 3],
    'price': [ 5000, 10000, 80000],
    'quantity': [10, 15, 12]
}
df = pd.DataFrame(table, columns=['id', 'price', 'quantity'])
print(df)

print(df['price'][0])
print(df['quantity'][2])

# print(df.loc[0])
# print(df.loc[1])
# print(df.loc[2])

print(df.loc[[0,1]])
print(df.loc[[0,1]][['id', 'price']])

# indexing
print(df.index)
print(df.columns)

# create dataframe from series
x = pd.Series([23, 45, 1, 55, 78])
df2 = pd.DataFrame(x)
print(df2)

df3 = pd.DataFrame(x, columns=['age'])
print(df3)

# Create dataframe from 2 dict
data = [
    {'a': "blue", 'b':"yellow", 'c': 'green'},
    {'a': "Python", 'b': "C++", 'c':"Java"}
]

df4 = pd.DataFrame(data)
print(df4)

# create dataframe from Numpy
numbers = [[123, 456],[789, 101112]]
df5 = pd.DataFrame(numbers, columns=['Pandas', 'Numpy'])
print(df5)

data = {'Country': ['Belgium', 'India', 'Brazil'], 
   'Capital': ['Brussels', 'New Delhi', 'Brasília'], 
   'Population': [11190846, 1303171035, 207847528]}

df6 = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
# select by position
print(df6.iloc[0,1])
print(df6.iat[0,1])

# select by label
print(df6.loc[0, 'Country'])
print(df6.loc[0, 'Population'])
print(df6.loc[0])

print(df6.at[0, 'Country'])
print(df6.at[0, 'Capital'])






# Load file in Dataframe
