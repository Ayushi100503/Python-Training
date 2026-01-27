import csv
import pandas as pd

df = pd.read_csv("retails.csv")
print(df)
print(df.info())#date should be date object not object
print(df.describe()) # only work on n umeric columns
print(df.isnull().sum()) #no null thus good data
df["Date"] = pd.to_datetime(df["Date"])
print(df.info())
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
print(df)


#high_elec = df[(df["Category"]=="Electronics")& (df["TotalPrice"]>10000)]
#print(high_elec)

#sorted_df = df.sort_values("TotalPrice", ascending=False)
#category_sales = df.groupby("Category")["TotalPrice"].sum()
#print(category_sales)
#store_avg = df.groupby("Store")["TotalPrice"].mean()
#print(store_avg)
#city_orders = df.groupby("City")["OrderID"].count()
#print(city_orders)

customers = pd.DataFrame({
    "CustomerType": ["New", "Returning"],
    "Discount": [5,10]
})
#merged = pd.merge(df, customers, on="CustomerType", how="inner")
merged = df.merge(customers, on="CustomerType", how="left")
print(merged)