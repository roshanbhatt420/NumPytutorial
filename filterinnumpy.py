import numpy as np
# filtering numpy array with arras boolean index lists
np3=np.array([1,2,3,4,5,6,7,8,9])
x=[True,True,False,True,True,False,True,True,False]
print(np3[x])
filter=[]
for thing in np3:
    if thing>0:
        filter.append(True)
    else:
        filter.append(False)

print(np3)
# for this numpy has shortcut 
filtered= np3%2 == 0
print(filtered)


