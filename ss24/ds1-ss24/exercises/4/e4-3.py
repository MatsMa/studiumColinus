import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 1
df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
)

# 2 a)
# Some statistical measures
# Describing central tendency
age_mean = df["age"].mean()
age_median = df["age"].median()
# mode?
# Describing dispersion
age_min = df["age"].min()
age_max = df["age"].max()
age_range = age_max - age_min
# range and IQR?
age_std_dev = df["age"].std()
# Describing shape
age_skew = df["age"].skew()
# kurtosis?

df["age_group"] = [
    "below_mean" if age < age_mean else "above_mean" for age in df["age"]
]

# Histogram with KDE
sns.histplot(data=df, x="age", kde=True)
# sns.histplot(data=df, x='age', estimator=np.mean, errorbar="sd", bins=20, hue='age_group', multiple='stack', palette=['skyblue', 'lightcoral'])
# sns.displot(kind="ecdf", data=df, x="age")
plt.axvline(
    age_mean,
    color="red",
    linestyle="dashed",
    linewidth=1,
    label=f"Mean Age: {age_mean:.2f}",
)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
# plt.legend([f"Mean: {age_mean:.2f}"])
# Create empty plot with blank marker containing the extra label
plt.plot(
    [],
    [],
    " ",
    label=f"Median: {age_median:.2f}\nStd. Dev: {age_std_dev:.2f}\nRange: {age_range} ({age_min}...{age_max})\nSkewedness: {age_skew:.2f}",
)
plt.legend()

plt.show()

# b)
percent_below_mean = (df["age"] < age_mean).mean() * 100
percent_above_mean = (df["age"] >= age_mean).mean() * 100
labels = ["Below Mean", "Above Mean"]
sizes = [percent_below_mean, percent_above_mean]
colors = ["skyblue", "lightcoral"]

plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
plt.title("Proportion of Passengers Below vs. Above Mean Age")

plt.show()

# c) TODO

# d)
# Box Plot or Violin Plot?
sns.violinplot(
    data=df, x="sex", y="age", hue="alive", split=True, inner="quart"
)
plt.title("Alive Status for Sex")
plt.show()

# e)
# sns.barplot(df, x="class", y="fare", errorbar="sd")
sns.catplot(data=df, x="class", y="fare", hue="class", kind="box")
