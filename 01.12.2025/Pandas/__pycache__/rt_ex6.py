import pandas as pd
df = pd.read_csv("sales_data.csv")
#6. Add a new column Discount:

#10 percent discount for Returning customers
#5 percent discount for New customers
#Compute final price after discount.


df["TotalPrice"] = pd.to_numeric(df["TotalPrice"], errors="coerce")
def calculate_discount(row):
    if row["CustomerType"] == "Returning":
        return 0.10
    elif row["CustomerType"] == "New":
        return 0.05
    else:
        return 0.0
df["Discount"]=df.apply(calculate_discount, axis=1)
df["FinalPrice"] = df["TotalPrice"] * (1-df["Discount"])
print(df.head())