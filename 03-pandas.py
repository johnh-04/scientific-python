# Pandas is a powerful library for data manipulation and analysis in Python. It provides data structures like Series and DataFrame, which allow you to work with structured data efficiently.

# pip install pandas

import pandas as pd

# Series
series = pd.Series([1, 2, 3, 4, 5])
print(series)  
# Output: 0    1
#         1    2
#         2    3
#         3    4
#         4    5
#         dtype: int64

# DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
# Output:
#       Name  Age         City
# 0    Alice   30     New York
# 1      Bob   25  Los Angeles
# 2  Charlie   35      Chicago

# Creating a DataFrame from a CSV file
df = pd.read_csv("data.csv")
print(df.head())  # Output: first 5 rows of the DataFrame

pd.read_csv("data.csv", sep=";")  # Read CSV with a different separator
pd.read_csv("data.csv", header=None)  # Read CSV without header
pd.read_csv("data.csv", names=["Column1", "Column2", "Column3"])  # Read CSV with custom column names
pd.read_csv("data.csv", index_col="Column1")  # Read CSV and set a column as index
pd.read_csv("data.csv", usecols=["Column1", "Column2"])  # Read only specific columns from CSV
pd.read_csv("data.csv", skiprows=1)  # Skip the first row of the CSV file
pd.read_csv("data.csv", nrows=10)  # Read only the first 10 rows of the CSV file
pd.read_csv("data.csv", na_values=["NA", "N/A"])  # Treat specific values as NaN
pd.read_csv("data.csv", parse_dates=["DateColumn"])  # Parse specific columns as dates
pd.read_csv("data.csv", dtype={"Column1": str, "Column2": int})  # Specify data types for columns
pd.read_csv("data.csv", encoding="utf-8")  # Specify encoding when reading CSV file

# Exploring DataFrame
print(df.info())  # Output: information about the DataFrame
print(df.describe())  # Output: statistical summary of the DataFrame
print(df.shape)  # Output: number of rows and columns in the DataFrame

# Accessing data (DataFrame)
print(df["Age"])  # Output: Series of the "Age" column
print(df[["Name", "City"]])  # Output: DataFrame with only "Name" and "City" columns
print(df.iloc[0])  # Output: first row of the DataFrame
print(df.iloc[0:2])  # Output: first two rows of the DataFrame
print(df.loc[0, "Name"])  # Output: value of "Name" in the first row
print(df.sort_values(by="Age"))  # Output: DataFrame sorted by "Age"

# Filter data (DataFrame)
print(df[df["Age"] > 30])  # Output: rows where "Age" is greater than 30
print(df[df["City"] == "New York"])  # Output: rows where "City" is "New York"

# Modify data
df["Age"] = df["Age"] + 1  # Increment age by 1
print(df)  # Output: DataFrame with updated ages

df.drop(columns=["City"], inplace=True)  # Drop the "City" column
print(df)  # Output: DataFrame without the "City" column

df.loc[df["Name"] == "Alice", "Age"] = 31  # Update age for Alice
print(df)  # Output: DataFrame with updated age for Alice

df.drop(index=0, inplace=True)  # Drop the first row of the DataFrame
print(df)  # Output: DataFrame without the first row

# Save data
df.to_csv("updated_data.csv", index=False)  # Save DataFrame to a new CSV file without the index