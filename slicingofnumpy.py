# slicing of numpy
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8])
# return 2,3,4,5,6
print(np1[1:6]) 
# return to the end
# nothing means for to the end
# we can slice from negative
print(np1[1:])
print(np1[-4:6])
# wee can return slices with steps
print(np1[1:8:2])
# steps on the entire array
print(np1[::3])
# this means every third number
# slice in the 2d arrray
np2=np.array([[2,3,4,5,6,4,3],[3,4,5,6,6,4,3]])
print(np2[0:7:2,0:7:2])