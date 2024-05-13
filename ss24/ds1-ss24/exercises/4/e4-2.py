import pandas as pd
import numpy as np

df = pd.read_csv("cleaned_titanic.csv", sep=";")

df.info()

print(df["Sex"].unique())

# Further cleaning
# valid_sex_entries = ["male", 'female', "mal", "femal", "mle"]
valid_sex_entries = ["male", 'female']
# Convert all entries to lowercase for comparison
df['Sex'] = df['Sex'].astype(str).str.lower()

# Replace invalid entries with NaN
df.loc[~df['Sex'].isin(valid_sex_entries), 'Sex'] = np.nan

# Fill NaN values with 'unknown'
df['Sex'].fillna('unknown', inplace=True)

print(df)
