#14. Write the filtered Electronics-only dataset into a new CSV file.
import pandas as pd
df = pd.read_csv("sales_data.csv")
electronics_df = df[df["Category"]=="Electronics"]
electronics_df.to_csv ("electronics_only.csv", index=False)
print(electronics_df)