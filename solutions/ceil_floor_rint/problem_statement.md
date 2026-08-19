# [Floor, Ceil and Rint](https://hackerrank.com)

## Problem Statement

### floor
The tool `floor` returns the floor of the input element-wise. The floor of a number x is the largest integer i such that i ≤ x.

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.floor(my_array))            # [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
```

### ceil
The tool `ceil` returns the ceiling of the input element-wise. The ceiling of a number x is the smallest integer i such that i ≥ x.

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.ceil(my_array))             # [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
```

### rint
The tool `rint` rounds elements of the array to the nearest integer.

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.rint(my_array))             # [ 1.  2.  3.  4.  6.  6.  8.  9.  10.]
```

---

### Task
You are given a 1-D array, A. Your task is to print the `floor`, `ceil` and `rint` of all the elements of A.

### Note
In order to get the correct output format matching the test cases, you must use the legacy NumPy printing setting:
```python
numpy.set_printoptions(legacy='1.13')
```
