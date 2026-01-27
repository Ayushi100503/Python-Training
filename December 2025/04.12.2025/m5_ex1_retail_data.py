
import pandas as pd
import numpy as np

products = ["Laptop", "Apple", "Mouse"]
categories = ["Electronics", "Grocery", "Electronics"]

data = {
    "OrderID": np.arange(1, 101),
    "ProductID": np.random.choice(products, 100),
    "Category": np.random.choice(categories, 100),
    "UnitPrice": np.random.randint(1000, 70000, 100),
    "Quantity": np.random.randint(1, 5, 100)  # Fixed here
}

retail_df = pd.DataFrame(data)
retail_df["TotalPrice"] = retail_df["Quantity"] * retail_df["UnitPrice"]
retail_df.to_csv("retail_data.csv", index=False)

df = pd.read_csv("retail_data.csv")

total_orders = df["OrderID"].nunique()
total_revenue = df["TotalPrice"].sum()
top5_products = df["ProductID"].value_counts().head(5)

print("Total Orders:", total_orders)
print("Total Revenue:", total_revenue)
print("Top 5 Products:\n", top5_products)
