#13. Create a pivot table:
#Rows: Category
#Columns: PaymentMethod
#Values: TotalPrice (sum)
import pandas as pd
df = pd.read_csv("sales_data.csv")
pivot = pd.pivot_table(df, index="Category", columns="PaymentMethod", values="TotalPrice", aggfunc="sum", fill_value=0)
print(pivot)