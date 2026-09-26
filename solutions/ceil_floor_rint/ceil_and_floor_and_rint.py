import numpy as np

np.set_printoptions(legacy="1.13")

scalar = np.array(list(map(float, input().split())))

print(np.floor(scalar))
print(np.ceil(scalar))
print(np.rint(scalar))
