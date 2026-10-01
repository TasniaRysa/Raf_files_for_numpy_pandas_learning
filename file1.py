import numpy as np
lst=np.array([1,2,3,4,5,6],dtype=np.float32)
#[[1,2,3],[4,5,6]] is a 2d array
#dtype----data type
print(lst.ndim, lst.shape, lst.size)
#shape gives 2,3 cz row no=2 and col no=3 size=2*3=6
a=np.zeros(10)
 #makes an arrray of 10 zeros
print(a)

a=np.ones(10)
 #makes an arrray of 10 zeros
print(a)
newar=np.concatenate((lst,a))#merges two arrays into newar
print(newar)

print(np.arange(10))#gives an array of 0 to 9
print(newar.astype(np.int32))#converts the data type of newar to int32S
print("\n")
print(np.random.random((2,3)))#gives a 2d array of random numbers between 0 and 1
print("\n")
print(np.arange(10,20,2))#gives an array of numbers from 10 to 19 with a step of 2
# params:rangestart , rangestop, step
print("\n")
print(np.diag([1,2,3,4]))#gives a 2d array with the given list as diagonal elements
print("\n")
print(np.diag(np.ones(3)))
print("\n")
#uniform distribution: all entries get same chaance
print(np.random.uniform(0,1,(2,3)))#gives a 2d array 2*3 of random numbers between 0 and 1
#normal distribution: entries are likely to be closer to our assigned central value
print("\n")
print(np.random.normal(1,0.2,(2,3))) #(mean,stddev,shape)
#randint and uniform both do the same thing, but randint:int (inclusive of start, exclusive of end), uniform:float
print("\n")
print(np.random.randint(0,10,(2,3)))#gives a 2d array 2*3 of random integers between 0 and 9

a = np.array([1,2,3,4,5,6])

a = a.reshape(2,-1)
print("\n")
print(a)


print("\n")
print(a>3)
print(np.isnan(a))##checks if it is not a number or not
print(a[0,:])#gives the first row of the 2d array a
print(a[:,0])#gives the first column of the 2d array a
print(lst[:3])#gives the first 3 elems of the 1d array a
print(lst[-3:])#last 3 elems of the 1d array a, - means llast


