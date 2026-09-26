import numpy

# Read dimensions N and M, and construct the array
n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

# Compute the min along axis 1, then find the max of that result and print
print(numpy.max(numpy.min(arr, axis=1)))
