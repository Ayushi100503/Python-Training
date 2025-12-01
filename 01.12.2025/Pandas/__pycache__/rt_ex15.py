import pandas as pd
df = pd.read_csv("sales_data.csv")
#
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
final_df = (
    df[df["Quantity"] >= 2]
    .query("Category == 'Apparel'")
    .assign(TotalValue = lambda x: x["Quantity"] * x["UnitPrice"])
    .sort_values(by = "TotalValue", ascending = False)
    .reset_index(drop = True)
)
print(final_df)