import pandas as pd
df = pd.read_csv("sales_data.csv")
#1. Load the dataset and display:
print(df.head(5))
print(df.tail(5))
print(df.columns)
print(df.shape)
