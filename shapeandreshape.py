
import numpy as np
# # create the one d array to get the shape of the array
np1=np.array([1,3,4,5,6,6,7,7])
print(np1.shape)
np2=np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
print(np2.shape)
# # reshape the 2 dimensional array
np3=np1.reshape(4,2)
print(np3)
# reshaping the 3 dimensional array
np4=np1.reshape(2,2,2)
# # platten to back inthe 1 array
# # again reshape with -1 argue ments
np=np4.reshape(-1)
# //suppose np4 is 3 d array

