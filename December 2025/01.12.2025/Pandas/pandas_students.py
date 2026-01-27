import pandas as pd
data ={
    "Name": ["Aisha", "Rahul", "John"],
    "Marks": [95, 82, 78],
    "City": ["Mumbai", "Delhi", "Chennai"]
}
df = pd.DataFrame(data)
df.to_csv("student.csv", index=False)
print("CSV file created")

df = pd.read_csv("student.csv")
print(df)