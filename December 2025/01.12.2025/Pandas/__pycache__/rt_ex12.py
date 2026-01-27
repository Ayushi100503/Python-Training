#12. Find the average revenue per order for each CustomerType.
import pandas as pd
df = pd.read_csv("sales_data.csv")
avg_revenue = df.groupby("CustomerType")["TotalPrice"].mean().reset_index()
avg_revenue.rename(columns={"TotalPrice": "AvgRevenuePerOrder"}, inplace=True)
print(avg_revenue)
