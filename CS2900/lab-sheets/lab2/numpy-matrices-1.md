## NumPy & Matrices

You can now set up arrays of 1+ dimensions. A simple $2 \times 3$ matrix can be defined as:

```
A = np.array([1,5,2,3], [4,5,6])
```
Defining a matrix is an extension of how vectors are defined - by adding additional rows. So, you can:
* print out an array's contents - `A`
* find out its dimensions - `A.ndim`
* find out its number of rows/cols - `A.shape`
* find out how many total entries it has - `A.size`

Same commands can be used for vectors. NumPy doesn't have a distinction between vectors + matrices - they're just a special instance of an array.

```
b = np.array([5.1,2.0,3.1])
b
b.ndim
b.shape
b.size
```
Numpy allows building arrays with 2+ indices. Also has a class of objects called **type matrix**. A number of functions exist to create matrices without having to explicity enter the data in them.

The code below creates an array **A** with the same number of rows and columns as above but with zeros:

```
A = np.zeros((2,3))
```

The code below creates an array A with the same number of rows and columns as above but with ones.

```
A = np.ones((2,3))
```

If you want to create a similarly sized matrix:
```
A = np.empty((2,3))
B = np.array([[1.5,2],[3,4], [5,6]])

A = np.zeros_like(B)

# \n\n just puts two line breaks between the output of B and A.
print(B,"\n\n",A)

A = np.ones_like(B)
print(B,"\n\n",A)

A = np.empty_like(B)
print(B,"\n\n",A)
```

---

### Identity Matrix for Square Matrices
You can update individual elements as if you were accessing a regular 2D array.

```
A = np.eye(4)
A

A[0,1] = 7.0
A
```

---

### Multiplying Matrices with Vectors

You can compute the vector created by multiplying a matrix with a vector.

```
b = np.array([5,2])
A = np.array([[0,4], [1,2]])

np.matmul(A, b)
```

That's a simple $2 \times 2$ example, but you can pick different matrix sizes.

```
b = np.array([5,2,1])
A = np.array([[0,4,0],[1,1,1]])
np.matmul(A,b)
```

You have to be careful about the dimensions.

```
A = np.array([[0,4],[0,1],[1,1]])

try:
  print(np.matmul(A,b))
except :
  print(tb.format_exc())
```

You can multiply matrices:

```
A = np.array([[0,4],[1,1]])
B = np.array([[1,2],[0,1]])
np.matmul(A,B)
```