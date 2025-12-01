import pandas as pd
df = pd.read_csv("sales_data.csv")
#8. Group by Category and compute:
df["TotalPrice"] = pd.to_numeric(df["TotalPrice"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
category_summary = df.groupby("Category").agg(Total_Quantity_Sold = ("Quantity", "sum"), Total_Revenue = ("TotalPrice", "sum")).reset_index()
print(category_summary)