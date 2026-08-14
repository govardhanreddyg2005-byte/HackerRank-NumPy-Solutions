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
