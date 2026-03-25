import numpy as np
import math
import re

# q: compute the floating point numbers cDE, cDu and cEu that are respectively the cosine of the angle between Dutch and English texts, the Dutch and unknown texts and the English and unknown texts. 
# From these values try and determine the language of the unknown text.

'''
info:
- in the Jupyter folder there are three files, Dutch.txt, English.txt and unknown.txt.
- the first two files are the same text in Dutch and English respectively. 
'''

def getString(fn):
  with open(fn, 'r') as f:
    return f.read().lower()

def getIncidence(string):
  letters = "abcdefghijklmnopqrstuvwxyz"
  Nc = len(letters)
  n = np.zeros(Nc, dtype=np.float64)
    
  for i, c in enumerate(letters):
    n[i] = len(re.findall(c, string)) * 1.0
  return n

def calcFreq(fileName):
  s = getString(fileName)
  n = getIncidence(s)
  total = np.sum(n)
  f = n / total
  return f

def calcCosFreqVec(f1, f2):
  dot = np.dot(f1, f2)
  norm_f1 = math.sqrt(np.dot(f1, f1))
  norm_f2 = math.sqrt(np.dot(f2, f2))
    
  if norm_f1 == 0 or norm_f2 == 0:
    return 0.0
    
  return dot / (norm_f1 * norm_f2)

fDutch = calcFreq("Dutch.txt")
fEnglish = calcFreq("English.txt")
fUnknown = calcFreq("unknown.txt")

# Cosine between Dutch and English
cDE = calcCosFreqVec(fDutch, fEnglish)

# Cosine between Dutch and Unknown
cDu = calcCosFreqVec(fDutch, fUnknown)

# Cosine between English and Unknown
cEu = calcCosFreqVec(fEnglish, fUnknown)

print("Cosine Dutch vs English (cDE):", cDE)
print("Cosine Dutch vs Unknown (cDu):", cDu)
print("Cosine English vs Unknown (cEu):", cEu)