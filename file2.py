import numpy as np
values= np.random.randint(1,5, 5)
output= np.empty(len(values)) #empties an array of the same length as values
for i in range(len(values)):
    output[i]=values[i]**2
output2=values**2

for i in range(len(values)):
    print(f"the square of {values[i]} is {output[i]}")
    print(f"the square of {values[i]} is {output2[i]}")
sum1=sum(output,output2)
print("my demands are the punchlines you agree to just to not see me scream:",sum1)

print(np.sum(values))
print(np.mean(values))
print(np.min(values))
print(np.max(values))