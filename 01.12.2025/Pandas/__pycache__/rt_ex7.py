import pandas as pd
df = pd.read_csv("sales_data.csv")
#7. Find how many orders were paid using:
#Cash
#Credit Card
#UPI
payment_counts = df["PaymentMethod"].value_counts()
print(payment_counts)