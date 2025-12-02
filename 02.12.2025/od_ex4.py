import pandas as pd

df = pd.read_csv("od.csv", )
print(df)

sorted_sales_desc = df.sort_values("Sales", ascending=False)
print(sorted_sales_desc)

sorted_profit_margin = df.sort_values("Profit")
print(sorted_profit_margin)

sorted_region_city = df.sort_values(by =["Region","City"])
print(sorted_region_city)

sorted_shipping_days = df.sort_values("ShipDate", ascending=False)
print(sorted_shipping_days)

sorted_customer_name = df.sort_values("CustomerName")
print(sorted_customer_name)