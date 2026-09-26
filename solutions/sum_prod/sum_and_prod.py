import numpy

# Read dimensions N and M
n, m = map(int, input().split())

# Read the N x M array elements
array_elements = [list(map(int, input().split())) for _ in range(n)]

# Convert the gathered list into a NumPy array
my_array = numpy.array(array_elements)

# Step 1: Perform sum along axis 0
sum_axis_0 = numpy.sum(my_array, axis=0)

# Step 2: Compute the product of the resultant array
result_product = numpy.prod(sum_axis_0)

# Print the final result
print(result_product)
