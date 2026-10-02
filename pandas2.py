import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]
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
print("cumsum:\n",df['Age'].cumsum())