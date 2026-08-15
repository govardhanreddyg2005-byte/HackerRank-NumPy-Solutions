# [Eye and Identity](https://hackerrank.com)

## Problem Statement

### identity
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0.

```python
import numpy
print(numpy.identity(3)) #3 is the rows and columns

# Output :
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
```

### eye
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper, or lower depending on the optional parameter k. A positive k increases the diagonal, while a negative k decreases it.

```python
import numpy
print(numpy.eye(8, 7, k = 1))    # 8 rows, 7 columns, 1 upper diagonal

# Output :
# [[ 0.  1.  0.  0.  0.  0.  0.]
#  [ 0.  0.  1.  0.  0.  0.  0.]
#  [ 0.  0.  0.  1.  0.  0.  0.]
#  [ 0.  0.  0.  0.  1.  0.  0.]
#  [ 0.  0.  0.  0.  0.  1.  0.]
#  [ 0.  0.  0.  0.  0.  0.  1.]
#  [ 0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.]]
```

---

