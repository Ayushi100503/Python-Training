#10. Filter rows where Product name contains the letter “a” or “A”.
import pandas as pd
df = pd.read_csv("sales_data.csv")
products_with_a = df[df["Product"].str.contains("a", case=False, na=False)]
print(products_with_a.head(), "\n")