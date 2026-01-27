import pandas as pd
df = pd.read_csv("sales_data.csv")
#2. Convert the Date column to datetime and extract:
#Year
#Month
#Day
#Add them as new columns.
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
print(df.head(5))
