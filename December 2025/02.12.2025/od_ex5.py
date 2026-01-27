import pandas as pd

df = pd.read_csv("od.csv", )

sales_per_region = df.groupby("Region")["Sales"].sum()
print(sales_per_region)

avg_profit_category = df.groupby("Category")["Profit"].mean()
print(avg_profit_category)

orders_per_customer = df.groupby("CustomerName")["OrderID"].count()
print(orders_per_customer)

sales_per_segment = df.groupby("Segment")["Sales"].sum()
print(sales_per_segment)

qty_per_subcategory = df.groupby("SubCategory")["Quantity"].sum()
print(qty_per_subcategory)


df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors='coerce')
df["ShipDate"] = pd.to_datetime(df["ShipDate"], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=["OrderDate", "ShipDate"])

df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
mean_shipping_by_category = df.groupby("Category")["ShippingDays"].mean()
print(mean_shipping_by_category)