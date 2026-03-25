## EX 1

### Q1 : Order of Growth
1. $\log n  + 7n \rightarrow O(n)$
2. $5n + 2n \log n \rightarrow O(n \log n)$
3. $2n^2 + 3n \log n + 1 \rightarrow O(n^2)$ 
4. $3n + 4 \rightarrow O(n)$

Sorted: $O(n), O(n \log n), O(n^2)$

---
### Q2 : Insertion Sort
[5 2 4 6 1 3] 

[2 5 4 6 1 3] 

[2 4 5 6 1 3] 

[2 4 5 6 1 3] 

[1 2 4 5 6 3] 

[1 2 3 4 5 6]

---
### Q3 : Algorithm Design
Given a list (A) of (n) numbers and  a target value, determine whether there exists two elements (x, y $\in$ A), such that (x + y = target).

Method 1: Brute force, where you're checking all possible pairs of elements. For each (i = 0) to (n - 1), and for each (j = i + 1) to (n - 1), test whether (A[i] + A[j] = target). If such a pair is found, return True; else return False after all pairs are checked.
* Time and space complexity: $O(n), \space O(n^2)$

Method 2: Sorting with two pointers, where you first sort the array, then use two pointers: one at the start, and one at the end of the array. While the two pointers don't meet, compute the sum of the elements at these positions. If the sum equals to the target, return True. If the sum is less than the target, move the left pointer to the right. If the sum is greater than the target, move the right pointer to the left.
* Time and space complexity: $O(n \log n), \space O(1)$

Method 3: Hash Set, where you traverse the list while sorting elements in a set. For each element (x), check whether (target = x) is already in the set. If it is, return True; else insert (x) into the set and continue..
* Time and space complexity: $O(n), \space O(n)$

To conclude, the brute forece approach is simple, but inefficient. The sorting-based method improved efficiency, while the hash set approach achieves optimal time at the cost of additional space.

---
### Q4
1. fnA upper bound: $T_A(n) = O(n)$
2. fnB upper bound: $T_B(n) = O(n^2)$

---
### Q5
1. $O(n \cdot 10) = O(n)$ | Insertion sort is very efficient when elements are close to their correct positions.
2. $O(nk)$