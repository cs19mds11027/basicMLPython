import numpy as np

# create matrix
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
vector=np.array([1,2,3,4,5,6])

print(matrix[:])
print ("**************************")
print(matrix[1:,:])
print ("**************************")
print(vector[2:5])
print ("**************************")
print(matrix[-1,:])
print ("**************************")
print(matrix[:,-1])
