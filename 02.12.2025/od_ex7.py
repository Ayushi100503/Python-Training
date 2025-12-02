import pandas as pd
df = pd.read_csv("od.csv")

discount_lookup = pd.DataFrame({
    "Segment":["Consumer", "Corporate", "HomeOffice"],
    "DiscountPercent":[5,8,10]
})
df = df.merge(discount_lookup, on="Segment", how="left")
print(df.head(10))

region_tax = pd.DataFrame({
    "Region":["West", "East", "Central", "South"],
    "TaxPayment": [7,5,6,8]
})
df = df.merge(region_tax, on="Region", how="left")
print(df.head(10))

product_profit = df.groupby("ProductName")["Profit"].mean().reset_index().rename(columns={"Profit":"AvgProfit"})
df = df.merge(product_profit, on="ProductName", how="left")
print(df.head(10))