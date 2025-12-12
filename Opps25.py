# PROGRAM 25: Pandas CSV Handling

import pandas as pd

# Reading CSV file
filename = input("Enter CSV filename: ")

try:
    df = pd.read_csv(filename)
    print("\nOriginal Data:")
    print(df)

    # Removing missing values
    df_clean = df.dropna()
    print("\nData After Removing Missing Values:")
    print(df_clean)

    # Display basic statistics
    print("\nBasic Statistics:")

    print("Mean:\n", df_clean.mean(numeric_only=True))
    print("\nMedian:\n", df_clean.median(numeric_only=True))
    print("\nMode:\n", df_clean.mode(numeric_only=True))

except FileNotFoundError:
    print("Error: File not found!")
