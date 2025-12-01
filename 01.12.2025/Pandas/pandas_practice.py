import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

#print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.describe())
print(df["Name"])
print(df[["Name", "Marks"]])
#filters
high_scorers = df[df["Marks"]>70]
print(high_scorers)
filtered = df[(df["Marks"]>70) & (df["Age"]>22)]
print(filtered)
df["Results"] = df["Marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print(df)
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)
df2 = df.copy()
df2.loc[2, "City"] = None
print(df2)
print(df2.isnull().sum())
df2_filled = df2.fillna("Unknown")
print(df2_filled)