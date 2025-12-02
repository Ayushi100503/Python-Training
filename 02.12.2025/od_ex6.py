import pandas as pd

df = pd.read_csv("od.csv")

pivot_sales = df.pivot_table(index="Region", columns="Category", values="Sales", aggfunc="sum")
print(pivot_sales)

pivot_profit = df.pivot_table(index="SubCategory", columns="Segment", values="Profit", aggfunc="sum")
print(pivot_profit)

pivot_orders_returned = df.pivot_table(index = "Returned", columns = "Region", values = "OrderID", aggfunc = "count")
print(pivot_orders_returned)

pivot_avg_price = df.pivot_table(index = "Category", values = "UnitPrice", aggfunc = "mean")
print(pivot_avg_price)

df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["OrderMonth"] = df["OrderDate"].dt.to_period("M")

pivot_qty_month = df.pivot_table(index = "OrderMonth",columns = "Region",  values = "Quantity", aggfunc = "sum")
print(pivot_qty_month)