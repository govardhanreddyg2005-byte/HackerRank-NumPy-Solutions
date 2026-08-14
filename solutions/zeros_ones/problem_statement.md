# [Zeros and Ones](https://hackerrank.com)

## Problem Statement

### zeros
The `zeros` tool returns a new array of given shape and type, filled with zeros.

```python
import numpy

print(numpy.zeros((1,2)))                    # Default type is float
# Output : [[ 0.  0.]]

print(numpy.zeros((1,2), dtype = numpy.int)) # Type changes to int
# Output : [[0 0]]
```

### ones
The `ones` tool returns a new array of given shape and type, filled with ones.

```python
import numpy

print(numpy.ones((1,2)))                    # Default type is float
# Output : [[ 1.  1.]]

print(numpy.ones((1,2), dtype = numpy.int)) # Type changes to int
# Output : [[1 1]]
```

---

# [Zeros and Ones](https://hackerrank.com)

## Problem Statement

### zeros
The `zeros` tool returns a new array of given shape and type, filled with zeros.

```python
import numpy

print(numpy.zeros((1,2)))                    # Default type is float
# Output : [[ 0.  0.]]

print(numpy.zeros((1,2), dtype = numpy.int)) # Type changes to int
# Output : [[0 0]]
```

### ones
The `ones` tool returns a new array of given shape and type, filled with ones.

```python
import numpy

print(numpy.ones((1,2)))                    # Default type is float
# Output : [[ 1.  1.]]

print(numpy.ones((1,2), dtype = numpy.int)) # Type changes to int
# Output : [[1 1]]
```

---

### Task
You are given the shape of the array in the form of space-separated integers, each integer representing the size of a given dimension. Your task is to print an array of the given shape and integer type using the `numpy.zeros` and `numpy.ones` tools.

### Input Format
A single line containing the space-separated integers representing the dimensions of the array.

### Output Format
First, print the array using the `numpy.zeros` tool and then print the array using the `numpy.ones` tool. All elements must be of the integer (`int`) data type.

### Sample Input
```text
3 3 3
```

### Sample Output
```text
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
```

---

## Code Syntax & Core Logic

### 1. Shape Parameter as a Tuple
Both `np.zeros()` and `np.ones()` require their shape dimension arguments to be packed cleanly into a single structural container (typically a **tuple**), rather than passing integers as separate flat parameters:
```python
# CORRECT: Passed as a structural tuple
np.zeros((3, 3, 3))

# INCORRECT: Throws a type error
np.zeros(3, 3, 3) 
```

### 2. Default Float to Integer Allocation (`dtype=np.int32`)
By default, NumPy dynamically initializes memory matrices with standard 64-bit floating-point numbers (`0.` or `1.`). Because the HackerRank specification strictly expects integer representations (`0` or `1`), you must explicitly configure the layout by declaring `dtype=int` during execution.

### 3. Star-Unpacking Dynamic Inputs
Because inputs can scale anywhere from a 1D vector up to a multi-dimensional 4D tensor, we convert the incoming numerical input array tokens into an integer list directly using `list(map(int, input().split()))`.

