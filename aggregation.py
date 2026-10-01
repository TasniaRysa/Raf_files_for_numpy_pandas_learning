## this section is bbasicallly to watch aggregation through min,max sum of 2d arrays
import numpy as np
a=np.array([[1,2,3],[5,6,7]])

print(a.min(axis=0))#gives the min of each column, axis=0 means column wise, axis=1 means row wise
print(a.sum(axis=1))


print(np.sum(a,axis=0))#gives the min of each column, axis=0 means column wise, axis=1 means row wise


