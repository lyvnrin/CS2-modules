import numpy as np

# q: define 5 x 3 matrix of zeroes, A_cp1. Create variables nrow and ncol that have the same rows and cols of A_cp1, respectively.

'''
info:
- Must use np.shape for this, not setting the variables manually
'''

A_cp1 = np.zeros((5,3))
nrow, ncol = np.shape(A_cp1)
print(nrow, ncol)
