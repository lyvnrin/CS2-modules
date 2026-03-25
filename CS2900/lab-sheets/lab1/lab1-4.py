import numpy as np
import math

# q: create a function dist that accepts a single argument v which is a numpy vector. dist will return the length of v

'''
notes:
- can determine a unit vector du for a vector d
  - du = d/math.sqrt(d.dot(d))
'''
d = np.array([2., 1.])
v = np.array([1, 2, 3, 4,])

def dist(v):
    length = math.sqrt(d.dot(d))
    print(length)
    
    return length

dist(v)
