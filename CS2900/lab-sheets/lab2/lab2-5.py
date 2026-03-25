import numpy as np
import math

# q: Write a Python function Rx, which has two arguments, as 3 x 3 NumPy matrix, and a 3D vector, x, and returns the vector y = Rx. 
# If R is the out from thetaRot when theta = pi/4 and x is [[1],[1][1]], compute Rx with pen and paper. Define a variable Rx_cp5 and set it to equal to the result of your functions Rx with the R, x define above. Check if the output of Rx is the same.

def Rx(R, x):
    y = np.matmul(R, x)
    print (y)
    return y

theta = math.pi / 4
c = math.cos(theta)
s = math.sin(theta)
R = np.array([[c,s,0],[-s,c,0],[0,0,1]])

x = np.array([[1],[1],[1]]) 

Rx_cp5 = Rx(R, x)
