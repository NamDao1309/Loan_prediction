import pandas as pd

# x = pd.Series([23, 45, 1, 55, 78])
# print(x)
# print(x.values)
# print(type(x.values))

# print(x[2])

# a= [1,6,9,8]
# y= pd.Series(a,index=["x","y","t","z"]) #gán phần tử a vào đặt tên
# print(y)

# fruits = {1:"mango",2:"banana",3:"tomato",4:"kiwi"}
# my_fruits= pd.Series(fruits)
# print(my_fruits)

# my_fruits2=pd.Series()
# my_fruits2=pd.Series(fruits,index=[0,1,2,3,4])
# print(my_fruits2)

# #slitring
# print(my_fruits2[3])
# print(my_fruits2[1:3])

#DATAFRAME
table={'id':[1,2,3],
       'price':[500,10000,20000],
       'quantity':[10,15,12]
    
}
df=pd.DataFrame(table, columns=['id','price','quantity'])
print(df)

print(df['price'][0])
print(df['quantity'][2])

#lấy giá trị theo hàng [df.loc]
print(df.loc[0])
print(df.loc[1])

print(df.loc[[0,1]]) #lấy hàng 0 và 1
print(df.loc[[0,]]) #lấy hàng 0

#indexing
print(df.index)
print(df.columns)

# tạo dataframe từ Series
x= pd.Series([23,14,1,45,56])
df2= pd.DataFrame(x)
print(df2)

df3=pd.DataFrame(x,columns=['age'])
print(df3)


# data =[
#     {'a':"blue",'b':"vang",'c':"xanh"}
#     {'a':"python",'b':"C++",'c':"java"}
# ]
# taoj data frame tu numby

numbers=[[123,456],[789,1010]]
df5=pd.DataFrame(numbers, columns=['pandas','numpy'])
print(df5)

data = {
'nuoc': ['Vietnam','Lao','campuchia'],
'thudo': ['hanoi','Vienchan','phomphenh'],
'Dan-so':[10000,5000,3000],
}

df6= pd.DataFrame(data,columns=['nuoc','thudo','Dan-so'])
print(df6)
print(df6.iloc[0,1])
print(df6.iat[0,1])