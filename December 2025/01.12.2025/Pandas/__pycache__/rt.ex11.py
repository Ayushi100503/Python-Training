import pandas as pd
df = pd.read_csv("sales_data.csv")
#11. Sort the dataset by Date and then by TotalPrice.
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df_sorted = df.sort_values(by=["Date", "TotalPrice"])
print(df_sorted)