#4. Find the top 5 highest-value orders by TotalPrice.
import pandas as pd
df = pd.read_csv("sales_data.csv")
df["TotalPrice"] = pd.to_numeric(df["TotalPrice"], errors="coerce")
top5 =  df.sort_values("TotalPrice", ascending=False).head(5)
print(top5)
