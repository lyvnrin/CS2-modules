## Higher Dimensional Example
*Character Frequencies in Different Languages*

If you're given a piece of text it's possible to compute the frequency of occurence of each lower case letters in that text.
* Turns out the letters' frequence is relatively fixed from language to language
* Shouldn't be seen as an absolutely fixed set of frequencies - every text can represent a different style
* Turns out these frequencies are constant between different texts take from the same language
* Can use it decrypt texts

### Mathematically
For each test $T$, can compute the frequency of each letter $f^T_a$, $f^T_b, ...$ where $f^T_a$ is the frequency of lower cases "a"s in $T$, so on. For the English alphabet, there are 26 letters, so you can construct a vector $f^T$ of those frequencies.

* So $f^T$ is a vector with 26 *entries*.

### Comparisions
Then, you can compare how similar 2 texts $A$ and $B$ are by comparing their frequencies.

Suppose that their corresponding frequency vectors are $\underline f^A$ and $\underline f^B$. You can easily compute cosine of the angle between the 2 vectors:

$$\cos \theta \;\; = \;\; \frac{{\underline{f^A}^\intercal} \cdot {\underline{f^B}}}{|\underline{f^A}||\underline{f^B}|} \;\; .$$

**Remember**
1. If $cos\theta = 1$ then  $\underline f^A$ and $\underline f^B$ are parallel to each other - indicates similar frequencies
2. It doesn't matter about the dimensions number - the above relationship still holds

### Code
This can be tested in *Python*.

**Instructions**: To compute the frequence of letters for a text. To compute the dot product between different frequency vectors. Checking if texts are from the same language or not.

Below are 2 functions that'll read in a text and return a string. Another function will return a vector with the incidence of lower case letters.
* (i.e. how many times the letter "a" occurs, so on) in a string.

```
import re

def getString(fn):
  f = open(fn, 'r')
  myString = f.read()
  return myString.lower()

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
```

Shown in `check6.py`, `check7.py`, and `check8.py`
