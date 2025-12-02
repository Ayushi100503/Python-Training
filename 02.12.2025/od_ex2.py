
import pandas as pd

df = pd.read_csv("od.csv", )
print(df)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])
df = df.dropna(subset=["OrderDate", "ShipDate"])
df["ShippingDays"] = (df["ShipDate"]-df["OrderDate"]).dt.days
print(df)

df["ProfitMargin"] = df["Profit"]/df["Sales"]
print(df)

df["CustomerName"] = df["CustomerName"].str.title()
print(df)

df = df[df["Sales"] > 0]
print(df)

df["DiscountPercent"] = df["Discount"]*100
print(df)