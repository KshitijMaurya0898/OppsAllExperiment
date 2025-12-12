# PROGRAM 13: Convert Pandas Series to List and Show Its Type

import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40, 50])

# Converting Series to list
lst = s.tolist()

print("Pandas Series:")
print(s)

print("\nConverted Python List:")
print(lst)

print("\nType of Python List:", type(lst))
