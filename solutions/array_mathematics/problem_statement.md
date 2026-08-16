# [Array Mathematics](https://hackerrank.com)

## Problem Statement
Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.

```python
import numpy as np

a = np.array([1, 2, 3, 4], float)
b = np.array([5, 6, 7, 8], float)

print(a + b)                     # [ 6.  8. 10. 12.]
print(np.add(a, b))              # [ 6.  8. 10. 12.]
```

**Task**  
You are given two integer arrays, \(A\) and \(B\), of dimensions \(N \times M\).  
Your task is to perform the following element-wise operations:
1. Addition (`+`) [1]
2. Subtraction (`-`) [1]
3. Multiplication (`*`) [1]
4. Integer Division / Floor Division (`//`) [1]
5. Modulo (`%`) [1]
6. Power (`**`) [1]

### Input Format
* The first line contains space-separated integers \(N\) and \(M\).
* The next \(N\) lines contain the space-separated elements of array \(A\).
* The following \(N\) lines contain the space-separated elements of array \(B\).

### Output Format
Print the result of the 6 mathematical operations in the exact order stated above.

### Sample Input
```text
1 4
1 2 3 4
5 6 7 8
```
### Sample Output
```text
[ 6  8 10 12]
[-4 -4 -4 -4]
[ 5 12 21 32]
[0 0 0 0]
[1 2 3 4]
[    1    64  2187 65536]
```

---
