

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


