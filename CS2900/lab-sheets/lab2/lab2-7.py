import numpy as np
import math

# q: create a 3x3 matrix R1m, that's the inverse of R1 by using a formula. Compute a 3x3 matrix R1inv, that's the inverse of R1 using the linalg.inv function.

'''
info:
- Think about the angle in the inverse
'''

theta = math.pi / 4

R1 = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0,              0,             1]
])

R1m = np.array([
    [np.cos(theta),  np.sin(theta), 0],
    [-np.sin(theta), np.cos(theta), 0],
    [0,              0,             1]
])


R1inv = np.linalg.inv(R1)

print(R1m)
print(R1inv)
