import numpy as np

# q: Write a function compare that accepts two 3 dimensional NumPy vectors x and y, and a 3×3 NumPy matrix R. 
# compare should return a tuple of the form (l1,l2,d1,d2) where l1 is the length of x, 
# l2 is length of x when multiplied by R. 
# d1 is the dot product of x and y and d2 is the dot product of Rx and Ry. 
# Apply this function for (matrices).
# and R = R1 (described above). l1 should be equal to l2 and d1 should be equal to d2

'''
info:
- x = [[1],[1],[1]]
- y = [[1],[1],[11]]
'''

def compare(x, y, R):
    # length of x
    xtx = np.matmul(x.T, x)
    l1 = np.sqrt(xtx[0,0])

    # compute Rx
    Rx = np.matmul(R, x)

    # length of Rx
    RxTRx = np.matmul(Rx.T, Rx)
    l2 = np.sqrt(RxTRx[0,0])

    # dot product of x and y
    d1 = np.matmul(x.T, y)[0,0]

    # compute Ry
    Ry = np.matmul(R, y)

    # dot product of Rx and Ry
    d2 = np.matmul(Rx.T, Ry)[0,0]

    return (l1, l2, d1, d2)


x = np.array([[1],[18],[14]])
y = np.array([[1],[1],[11]])


R = np.eye(3)

compare(x, y, R)
print(compare(x, y, R))
