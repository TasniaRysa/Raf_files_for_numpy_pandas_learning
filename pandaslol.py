import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(s.head()) # View first 5 rows
print(s.tail(3))
 # View last 3 rows
s[2]=np.nan # Assign NaN to the 3rd element

temperatures_celsius = pd.Series([25, 26, 27, 28, 29, 30, 31], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
print("Temperature Series (Celsius):",temperatures_celsius)
print(temperatures_celsius.describe()) # Summary statistics like central tendency, dispersion, and shape of the dataset’s distribution
print(s.value_counts()) # Count of unique values in the Series
print(s.unique()) # Unique values in the Series
print(s.nunique()) # Number of unique values in the Series
print(s.isnull()) # Check for null values in the Series
print(s.notnull()) # Check for non-null values in the Series
print(s.sort_values())
print(temperatures_celsius.sort_index()) 
# Sort the Series by index

print(s.fillna(69)) # Fill NaN values with 69
print(s[:3]) # View first 3 entries (slicing), 
print(s[3:]) # View entries from index 3 to the end
print("now")
print(s[s>3]) #index by condition, view entries greater than 3

s.plot()
#plt.show()


df=pd.read_csv("student_scores.csv")
print(df)
print(df.values)

print("the info")
print(df.info)

print("dropna")
print(s.dropna()) # Drop rows with NaN values
