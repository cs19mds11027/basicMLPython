import numpy as np
from scipy import sparse

#row-major and column-major 1D array
vector_row=np.array([[1,2,3]])
vector_column=np.array([[1],[2],[3]])
print(vector_row.shape)
print(vector_column.shape)

# numpy matrix
matrix=np.array([[1,2],[1,2],[1,2]])
print(matrix.shape)
print(type(matrix))

mat=np.mat([[1,2],[1,2],[1,2]])
print(mat.shape)
print(type(mat))

# sparse matrix
mat=np.array([[0,1,0],[1,0,0],[2,0,1]])
sparse_mat=sparse.csr_matrix(mat)
print(sparse_mat)






