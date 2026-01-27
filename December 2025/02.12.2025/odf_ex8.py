import pandas as pd
df = pd.read_csv("od.csv")
import matplotlib.pyplot as plt
df["OrderYear"] = df["OrderDate"].astype(str)
df["OrderMonth"] = df["OrderDate"].astype(str)
df["OrderDay"] = df["OrderDate"].astype(str)
print(df.head(10))

df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors='coerce')
df["OrderWeekday"] = df["OrderDate"].dt.day_name()
print(df.head(10))

df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors='coerce')
df["ShipDate"] = pd.to_datetime(df["ShipDate"], errors='coerce')

df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
long_shipping_orders = df[df["ShippingDays"]>5]
print(df.head(10))