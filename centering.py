import numpy as np
a=np.array([[10,20],[15,25],[20,30]])
m=a.mean(axis=0)
print(a-m)
onear=np.ones((4,3))