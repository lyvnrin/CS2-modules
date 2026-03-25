import numpy as np

# q: define a variable a_2 and set it equal to the second entry in a.

'''
notes: 
-  can define a vector as follows. can access individual components directly like any other array.

- 'a' can be integers, floats, etc. Python is dynamically typed language, can figure out type via:
  - a.dtype.name
'''

a = np.array([1, 2, 3])
a_2 = a[1]
print(a_2)

