import numpy as np
import math

# q: create a function unitVec that acceps a single argument v which is a numpy vector. The function should behave like so:
#  1. is the vector is a null vector, it should return the string: "This is a Null vector"
#  2. for any other vector, it should return the unit vector that's paralle with v

'''
notes:
- can used the function dist written in check4.py
'''

# compute length of vector v
def dist(v):
    length = math.sqrt(v.dot(v))
    #print(length)
    
    return length

# return unit vector of v
def unitVec(v):
    # magnitude of vector
    length = dist(v)

    if length == 0:
        return "This is a Null vector"
    else:
        # divide by magnitude to get unit vector
        return v / length


v = np.array([1, 2, 3, 4,])
print(unitVec(v))

v_null = np.array([0, 0, 0, 0])
print(unitVec(v_null))