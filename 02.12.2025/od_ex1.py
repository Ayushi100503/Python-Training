
import pandas as pd

df = pd.read_csv("od.csv", )
print(df)

print(df.head(10))

print("Shape:", df.shape)

print(df.dtypes)

print("missing values:", df.isnull().sum())
print(df.isnull().sum())

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])
print(df)

