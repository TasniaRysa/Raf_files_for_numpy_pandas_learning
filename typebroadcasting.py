import numpy as np
a=np.array([[1,2,3],[5,6,7]])


newar=np.array([1,2,3])

print(a+newar)#broadcasting, adds newar to each row of a
#a becomes [1,2,3],[1,2,3]


#broadcasting in conditionals

#np.where(condition, value_if_true, value_if_false)

arr=np.array([12,23,36])
b=np.array(["Adult","child"])
res=np.where(arr>18,b[0],b[1])#if arr>18 then b[0] else b[1]
print(res)