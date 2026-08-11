# [Shape and Reshape](https://hackerrank.com)

## Problem Statement

### shape
The `shape` tool gives a tuple of array dimensions and can be used to change the dimensions of an array.

**(a). Using shape to get array dimensions**
```python
import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print(my__1D_array.shape)     # Output: (5,)

my__2D_array = numpy.array([[1, 2], [3, 4], [6, 5]])
print(my__2D_array.shape)     # Output: (3, 2)
```

**(b). Using shape to change array dimensions**
```python
import numpy

change_array = numpy.array([1, 2, 3, 4, 5, 6])
change_array.shape = (3, 2)
print(change_array)      

# Output:
# [[1 2]
#  [3 4]
#  [5 6]]
```

### reshape
The `reshape` tool modifies the shape of an array without changing its original data.

```python
import numpy

my_array = numpy.array([1, 2, 3, 4, 5, 6])
print(numpy.reshape(my_array, (3, 2)))

# Output:
# [[1 2]
#  [3 4]
#  [5 6]]
```

---

### Task
You are given a space-separated list of nine integers. Your task is to convert this list into a 3 × 3 NumPy array.

### Input Format
A single line of input containing 9 space-separated integers.

### Output Format
Print the 3 × 3 NumPy array.

### Sample Input
```text
1 2 3 4 5 6 7 8 9
```

### Sample Output
```text
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

---

## Core Logic & Concepts Explained

### 1. Integer Conversion via Explicit Initialization (`dtype=int`)

* **Memory Allocation:** By declaring `np.array(input_list, dtype=int)`, you explicitly dictate how bytes are mapped in the C-array backend. 
* **Native Conversion:** If strings pass into an array construction with `dtype=int`, NumPy automatically converts the base elements into integer objects during memory allocation. This approach bypasses standard Python execution loop overhead entirely.

### 2. Dimension Alteration Mechanics (`np.reshape`)
Using `.reshape()` is significantly more efficient than standard manual array restructuring:

* **Memory Efficiency ("Views"):** Instead of copying elements into a new block of physical memory, `reshape()` returns a new **view** of the same underlying data buffer. The raw numbers `[1, 2, ... 9]` remain laid out continuously in physical RAM.
* **Stride Mapping:** Changing dimensions simply alters the array's internal metadata (`strides`). The strides array tells NumPy exactly how many contiguous bytes it needs to jump forward in the memory block to move down to the next row or slide over to the next column.