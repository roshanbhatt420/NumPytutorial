# copy vs view
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9,0])
# create view
np2=np1.view()
print(f'original NP1{np1}')
print(f'original NP2{np2}')
np1[0]=43
print(f'CHANGED np1{np1}')
# print(f'original np2{np2}')//view is the copy of the original but changes done in inherited data change the original np1
# create copy
np2=np1.copy()
print(f'original np1{np1}') 
print(f'original np1{np2}') 
np1[0]=45
print(f'change np1{np1}') 
print(f'change np1{np2}') 