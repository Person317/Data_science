

import pandas as pd
df = pd.read_csv ("data.csv")
import matplotlib.pyplot as plt
import numpy as np

# Cleaning data
print("List of missing column values")
print("-------------------------")
print(df.isnull().sum())

print()
print("Number of duplicate rows")
print("-------------------------")
print(df.duplicated().sum())

#Pie chart 1
y = np.array([39, 36.3, 33.1, 25.2, 21.5])
mylabels = ["Boliva", "Mexico", "Venezuela", "Ecuador", "New Zeland"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Highest Poverty Rates")
plt.show()

y = np.array([10.99, 10.43, 10.99, 10.99, 12.53])
mylabels = ["Boliva", "Mexico", "Venezuela", "Ecuador", "New Zeland"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Corresponding Subscription Rates")
plt.show()