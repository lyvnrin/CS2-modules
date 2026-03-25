import numpy as np

# q: create another vector co that is orthogonal to c
# q: create a floating point number p that demonstrates that co is orthogonal to c. (hint: p should b 0.0)

'''
notes:
- there isn't a length function in numpy, but you can easily construct one
  - import math
  - math.sqrt(d.dot(d))

- vectors are objects, only copy them passing the reference or the 'copy' method
  - u = c.copy()

- computing the dot product between any 2 vectors
  - c = np.array([1, 2, ..])
  - c.dot(d)

- 2 vectors are orthogonal is their dot product is 0:
  - c * co = 0
'''

c = np.array([1., 2.])

# if c = [c1, c2], orthogonal vector = swap components + flip sign of one
co = np.array([-c[1], c[0]])

# dot product
p = np.dot(c, co)

print(co, p)