import pandas as pd

# SERIES
x = pd.Series([23, 45, 1, 55, 79])
print(x)
print(x.values)
print(type(x.values))
print(x[0])

a = [1, 6, 3, 7]
y = pd.Series(a, index=["x","y", "z", "t"])
print(y)
print(y["x"])

#DATAFRAME
table = pd.DataFrame({
    'id':[1,2,3],
    'price':[5000, 10000, 8000],
    'quantity':[10, 15, 12]
})
print(table)
print(table['id'][0])

# lay theo row
# print(table.loc[0])
# print(table.loc[2])
print(table.loc[[0,1]])

# print(table.iloc[0])
# print(table.iloc[2])
print(table.iloc[[0,1]])
print(table.iloc[[0,1]][['id', 'quantity']])

print(table.at[1, 'price'])
print(table.iat[1, 1])

# indexing
print(table.index)
print(table.columns)

# create dataframe from series
df2 = pd.DataFrame(x)
print(df2)

# create dataframe from 2 dict
data = [
    {'a':"blue", 'b':"yellow", 'c':"green"},
    {'a':"Python", 'b':"C#", 'c':"Java"}
]
df3 = pd.DataFrame(data)
print(df3)

s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c','d'])
s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
print(s+s3)
s1 = s.add(s3, fill_value=0)
print(s1)

# Read file CSV, TXT, EXCEL

csv_path = "Buoi08.06.12.2023\Automobile_data.csv"
df_csv = pd.read_csv(csv_path)
print(df_csv)
print("Rowx Column:", df_csv.shape )
print("Index:", df_csv.index )
print("Column:", df_csv.columns )
print("Info:", df_csv.info() )
print("Describe:", df_csv.describe() )


excel_path = "Buoi08.06.12.2023\demo.xlsx"
df_excel = pd.read_excel(excel_path)
print(df_excel)

txt_path = "Buoi08.06.12.2023\data.txt"
df_txt =pd.read_csv(txt_path, sep=',')
print(df_txt)
print("5 first rows :", df_txt.head(5))
print("5 last rows :", df_txt.tail(5))
