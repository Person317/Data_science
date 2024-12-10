

import pandas as pd
df = pd.read_csv ("data.csv")
import matplotlib.pyplot as plt

# Cleaning data
print("List of missing column values")
print("-------------------------")
print(df.isnull().sum())

print()
print("Number of duplicate rows")
print("-------------------------")
print(df.duplicated().sum())

# 1st Pie chart
df1 = df.groupby("Name").sum()
df1.plot.pie(y="GDP", lables=df1.index)
plt.show()

