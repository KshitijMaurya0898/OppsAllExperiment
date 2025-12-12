# PROGRAM 26: Pandas DataFrame Operations

import pandas as pd

# Creating dictionary of student details
data = {
    "Name": ["Aman", "Riya", "Karan", "Sneha", "Arjun"],
    "Age": [20, 19, 21, 20, 22],
    "Marks": [85, 92, 78, 88, 90]
}

# Creating DataFrame
df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)

# a) First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# b) Last 3 rows
print("\nLast 3 rows:")
print(df.tail(3))

# c) Shape of DataFrame
print("\nShape (rows, columns):", df.shape)

# d) Size of DataFrame
print("Size (total elements):", df.size)
