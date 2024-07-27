
# # simple python list in python
list=[2,3,4,2,3,4,3,4]
print(list)
list2=[2,3,4,"roshan","bhatta"]
print(list2)
# # why numpy 
# # to reduce the computational cost and calculation
# # its more powerful than list 
# datatype in the numpy is ndarray which means n dimensional array
import numpy as  np
np1=np.array([0,1,24,3,4,5,6,7,8,9])
np2=np.arange(27,)
print(np1)
# # print(np1.shape)//.shape method gives the length of the array
# we can create the array of zero//.zero gives the required no of the zero
print(np2)
np4=np.zeros(9,)
print(np4)
# multidimensional array
# zeros array in multidimensional array
 np5=np.zeros((2,12))
# //.zero gives the multidimantional zeros in  this case it gives two d
print(np5)
# full (.full first arguement gives the dimention second give the no of  and third give the which number want to show you )
np7=np.full((2,20),4)
print(np7)
# we can convert the python list in the numpy
my_list=[1,2,3,4,4,4]
np8=np.array(my_list)
print(np8)
print(np8[0])

