
import pandas as pd

df = pd.read_csv("od.csv", )
print(df)

west_orders = df[df["Region"] == "West"]
print(west_orders)

tech_sales_400 = df[(df["Category"] == "Technology") & (df["Sales"]>400)]
print(tech_sales_400)

returned_products = df[df["Category"] == "Yes"]
print(returned_products)

furniture_after_date = df[(df["Category"] == "Furniture") & (df["ShipDate"]>"2024-01-20")]
print(furniture_after_date)

low_profit_orders = df[df["Profit"]<200]
print(low_profit_orders)