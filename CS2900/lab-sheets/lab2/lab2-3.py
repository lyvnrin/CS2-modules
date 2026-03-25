import numpy as np
import matplotlib.pyplot as plt

#q: Define R and x as below. Create a vector y such that: (underline) y = (bold)R (underline) x or y = Rx.

'''
info:
- matrix R
  R = [ 3   2   1
      1  -1   2 ]

- matrix x
x = [ 1
      2
     -1 ]
'''

R = np.array([[3,2,1], [1,-1,2]])
#print(R)

x = np.array([[1],[2],[-1]])
#print(x)

y = np.matmul(R, x)
print(y)