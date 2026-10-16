import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000],
        'Gender':['F', 'M', 'M', 'M', 'F']
        }
df = pd.DataFrame(data) #aligns rows and columns in a tabular format, without rigid indexxing wwith num
print(df.shape)
print(df.columns)
print(df.index) #row labels of the DataFrame
print(df.info)

print("min age", df['Age'].min()) # Minimum value in the 'Age' column


datano3=[[1,2,3],[4,5,6],[7,8,9]]

df2=pd.DataFrame(datano3)
print(df2.sum(axis=1)) # Sum of each row
print("cumsum:\n",df['Age'].cumsum()) #cumulative sum of the 'Age' column
print("stddev:\n",df['Age'].std())#standard deviation
print(df.map(lambda x: x*2)) # Apply a function to each element of the DataFrame
col=df[['Age','Salary']].map(lambda x: x**2) #selects columns 'Age' and 'Salary' and put it in col
print(col)


print(df[(df['Age'] > 30) & (df['Gender']=='F')] ) # Filter rows where 'Age' is greater than 30
df['kids']=[0, 1, 2, 3, 4] # Add a new column 'kids' to the DataFrame
print(df)
df['Salary']=df['Salary'].astype(float)
 # Change the data type of the 'Salary' column to float
print(df)

df.to_csv('output.csv', index=False) # Save the DataFrame to a CSV file without the index