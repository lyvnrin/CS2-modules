import numpy as np

# q: create another vector b which is equal to [4, 5, 6] where the entries are of type float

'''
notes:
- hint: refer to the numpy docs on how to specify the dtype of an array

- there's a transpose operation, but for vectors defined this way, it doesn't do anything.
  - a.T
'''

b = np.array([4, 5, 6], dtype=float)
print(b, b.dtype)