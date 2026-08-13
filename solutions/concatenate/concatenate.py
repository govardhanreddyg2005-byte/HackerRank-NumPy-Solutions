import numpy as np

N,M,P = map(int, input().split())

columns_A = []

for _ in range(N):
    columns_A.append(input().split())
    
columns_B = []

for _  in range(M):
    columns_B.append(input().split())
    
A = np.array(columns_A, dtype=int)
B = np.array(columns_B, dtype=int)
    
combined = np.concatenate([A,B], axis=0)
print(combined)
