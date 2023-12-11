import pandas as pd

from sqlalchemy import create_engine
import pymysql


# export file csv, excel, sql

data = {
    "name":["laptop", "table", "keyboard", "desk"],
    "brand": ["A", "B", "C", "D"],
    "price":[1200, 450, 100, 600]
}
df = pd.DataFrame(data)
df.to_csv("Buoi09.11.12.2023\products.csv", index=False)

print(df)
