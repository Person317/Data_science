

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

#Pie chart 2
y = np.array([10.99, 10.43, 10.99, 10.99, 12.53])
mylabels = ["Boliva", "Mexico", "Venezuela", "Ecuador", "New Zeland"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Corresponding Subscription Rates")
plt.show()

#Bar Graph 1
x = np.array(["United States", "Hong Kong", "Germany", " Australia", "France"])
y = np.array([73600, 64400, 61900, 59500, 55200])
plt.bar(x,y)
plt.show()

#Bar Graph 2
x = np.array(["United States", "Hong Kong", "Germany", " Australia", "France"])
y = np.array([13.99, 11.93, 14.67, 12.12, 15.24])
plt.bar(x,y)
plt.show()

#Line Graph
x = np.array([123.2, 68.4, 52.0, 10.8, 9.4, 6.7])
y = np.array([13.13, 13.2, 11.47, 11.49, 19.54, 11.29])
plt.plot(x)
plt.plot(y)
plt.show()