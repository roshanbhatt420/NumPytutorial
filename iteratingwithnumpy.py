import numpy as np
# 1 d array
np1=np.array([1,2,3,4,5,6,7,8,9,10])
for x in np1:
#     print(x)//simple python
np2=np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
for x in np2:
    # print(x)
    for y in x:
        print(y)
np3=np.array([[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]])
for i in np3:
    for j in i:
        for k in j:
            print(k)
# use of np.nditer()
for i in np.nditer(np3):
    print(i)
