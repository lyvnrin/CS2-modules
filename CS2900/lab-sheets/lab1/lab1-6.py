import numpy as np
import matplotlib.pyplot as plt
import re
import os

# q: Create a function calcFreq that accepts a single argument fileName which is the file name of the text file name. calcFreq returns the frequency vector for fileName. 
# If n​ is the vector of incidences then (latex_formula). If you look in the NumPy documentation you will a function to compute the denominator of this.

r'''
notes:
- latex formula shown via matplotlib
  - plt.figure(figsize=(12, 6), dpi=150)
  - plt.text(0.1, 0.5, r'$f_i \;\; = \;\; \frac{n_i}{\sum_j n_j} \;\;$')
  - plt.axis('off')
  - plt.show()
'''

def getString(fn):
  here = os.path.dirname(__file__)
  path = os.path.join(here, fn)

  with open(path, 'r') as f:
    return f.read().lower()

def getIncidence(string):
  letters = "abcdefghijklmnopqrstuvwxyz"
  Nc = len(letters)
  n = np.zeros(Nc,dtype=np.float64)
  i = 0
  
  for c in letters:
    x = re.findall(c,string)
    n[i] = len(x) * 1.0
    i += 1
  return n

def calcFreq(fileName):
    s = getString(fileName)
    n = getIncidence(s)
    total = np.sum(n)
    f = n / total
    return f

f = calcFreq("example.txt")
print(f)

