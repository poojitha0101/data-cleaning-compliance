import pandas as pd

data = {
    "CustomerID": [1, 2, 2, 3, 4],
    "Name": ["John", "Alice", "Alice", None, "Bob"],
    "Age": [25, None, 30, 22, 35],
    "City": ["NY", "LA", "LA", "NY", None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Not Specified")

print("\nCleaned Data:")
print(df)
