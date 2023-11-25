import pandas as pd
import numpy as np

# dta_parth = "D:\DA\VIETECH_DA_28.09.2023\Student's homeworks\Chu Hai\buoi15\hocsinh.csv"
# df1= pd.read_csv(csv_parth)

# from sqlalchemy import create_engine
# # engine = create_engine('sqlite:///:demo:')
# import pymysql
# # tableName="users"
# # datafame= pd.DataFrame(data=d)
# sqlengine= create_engine('mysql+pymysql://root:@127.0.0.1/demo',pool_recycle =3306)
# dbConnection = sqlengine.connect()
# df = pd.read_sql("SELECT*FROM user",dbConnection)
# print(df)
from sqlalchemy import create_engine
import pymysql
import pandas as pd

csv_path =""

sqlengine = create_engine('mysql+pymysql://root:@127.0.0.1/demo', pool_recycle=3306)
dbConnection = sqlEngine.connect()
df = pd.read_sql("SELECT * FROM users", dbConnection)  # Sửa lỗi ở đây, đổi "user" thành "users"
print(df)

dbConnection.close()

