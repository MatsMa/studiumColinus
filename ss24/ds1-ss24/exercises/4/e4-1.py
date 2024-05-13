import pandas as pd

df = pd.read_csv("tips.csv")
print(df.shape)

# Check if each dtype is numeric
data_types = df.dtypes
count_numeric = 0
for col, dtype in data_types.items():
    is_numeric = pd.api.types.is_numeric_dtype(dtype)
    if is_numeric:
        count_numeric += 1
    print(f"{col} is numeric: {is_numeric}")

print(
    f"Numeric columns: {count_numeric}, other: {len(data_types) - count_numeric}"
)
