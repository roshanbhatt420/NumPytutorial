import numpy as np
np2=np.array([2,3,6,4,5,4,3,3,2,2,4,4,5,56,6])
x=np.where(np2==3)
print(x)
print(np2[x])
y=np.where(np2%2==0)
print(y)
# we can return as our choice 