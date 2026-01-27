import pandas as pd
df = pd.read_csv("sales_data.csv")
#9. Identify the store with the highest total sales.
df["TotalPrice"] = pd.to_numeric(df["TotalPrice"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
store_sales = df.groupby("Store")["TotalPrice"].sum()
top_store = store_sales.idxmax()
print(f"The top store is {top_store} (Sales: {store_sales.max()})\n")