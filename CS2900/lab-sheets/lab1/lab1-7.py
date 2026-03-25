import numpy as np
import math

# q: write a function calcCosFreqVec that accepts two arguments f1 and f2 which are two text frequency vectors. calcCosFreqVec returns the cosine of the angle between f1 and f2. You will need the math library.

def calcCosFreqVec(f1, f2):
    dot = np.dot(f1, f2)
    norm_f1 = math.sqrt(np.dot(f1, f1))
    norm_f2 = math.sqrt(np.dot(f2, f2))

    if norm_f1 == 0 or norm_f2 == 0:
        return 0.0
    
    return dot / (norm_f1 * norm_f2)


