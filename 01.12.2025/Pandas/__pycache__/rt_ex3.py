import pandas as pd
df = pd.read_csv("sales_data.csv")
#3. Calculate total sales (sum of TotalPrice) for each:
#Store
#City
#Category
df["TotalPrice"] = pd.to_numeric(df["TotalPrice"], errors="coerce")
result = (
    df.groupby(["Store", "City", "Category"])["TotalPrice"]
    .sum()
    .reset_index()
)
print(result)
