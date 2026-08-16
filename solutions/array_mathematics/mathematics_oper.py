import numpy as np

n,m = map(int, input().split())

columns_A = []

for _ in range(n):
    element = columns_A.extend(input().split())

columns_B = []

for _ in range(n):
    element = columns_B.extend(input().split())

array_A = np.array(columns_A, dtype=int).reshape(n,m)

array_B = np.array(columns_B, dtype=int).reshape(n,m)

print(array_A + array_B)
print(array_A - array_B)
print(array_A * array_B)
print(np.floor_divide(array_A, array_B))
print(array_A % array_B)
print(array_A ** array_B)
