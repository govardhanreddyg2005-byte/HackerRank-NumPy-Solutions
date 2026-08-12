import numpy as np

n,m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(input().split())
    
array = np.array(arr, dtype=int).reshape(n,m)

inverse = array.T

print(inverse)

print(array.flatten())
