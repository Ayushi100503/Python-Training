import pandas as pd
df = pd.read_csv("sales_data.csv")

#5. Filter the dataset to show only Electronics products with Quantity > 1.
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
electronics_filtered = df[(df["Category"] == "Electronics") & (df["Quantity"] > 1)]
print(electronics_filtered)
