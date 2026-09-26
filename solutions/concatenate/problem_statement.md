# [Concatenate](https://hackerrank.com)

## Problem Statement
Concatenate joins a sequence of arrays along an existing axis.

```python
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print(numpy.concatenate((array_1, array_2), axis = 0))   
# Output:
# [[1 2 3]
#  [0 0 0]
#  [0 0 0]
#  [7 8 9]]

print(numpy.concatenate((array_1, array_2), axis = 1))   
# Output:
# [[1 2 3 0 0 0]
#  [0 0 0 7 8 9]]
```

**Task**  
You are given two integer arrays of size \(N \times P\) and \(M \times P\) (\(N\) & \(M\) are rows, and \(P\) is the column). Your task is to concatenate the arrays along axis \(0\).

### Input Format
* The first line contains space-separated integers \(N\), \(M\) and \(P\).
* The next \(N\) lines contain the space-separated elements of the \(N \times P\) array.
* The following \(M\) lines contain the space-separated elements of the \(M \times P\) array.

### Output Format
Print the concatenated array matrix.

### Sample Input
```text
4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4
```

### Sample Output
```text
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
```

---

## Code Syntax & Core Logic

### 1. `np.concatenate` Syntax Mechanics
The standard syntax requires a tuple or list of arrays as its initial parameter:
```python
numpy.concatenate((array_1, array_2, ...), axis=0)
```
* **The Sequence Constraint:** The inputs **must** be wrapped inside a container like a tuple `(array_1, array_2)` rather than passed as direct independent arguments.
* **The Dimension Constraint:** All structural dimensions *except* the targeted concatenation axis must match identically.

### 2. Computational Axis Logic (\(Axis=0\))
* **Row-Wise Stacking (\(Axis=0\)):** Passing `axis=0` pieces arrays together vertically (adds rows). The matrix width (\(P\) columns) remains unchanged, while the height expands from \(N\) and \(M\) into a combined array structure of size \((N+M) \times P\).
* **Memory Management:** Unlike `reshape()`, concatenation creates a completely new array allocation block in computer memory rather than an isolated view, copying over the underlying data buffers sequentially.


