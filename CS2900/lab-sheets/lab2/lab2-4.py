import numpy as np
import math

# q: Write a python function thetaRot that acceps a single argument theta which is a floating point number and returns a 3 x 3 NumPy matrix (i.e theta = 0)

'''
info:
- Need the math library.
- cos pi/4 = sin pi/4 = 1/ sqrt(2)
- check if thetaRot returns that matrix
'''

def thetaRot(theta):
    c = math.cos(theta)
    s = math.sin(theta)

    R = np.array([[c,s,0],[-s,c,0],[0,0,1]])

    return R


theta = math.pi / 4
R45 = thetaRot(theta)
print(R45)
