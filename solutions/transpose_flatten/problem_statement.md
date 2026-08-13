# [Transpose and Flatten](https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem)

## Problem Statement

* **Task:** Given an \(N \times M\) integer array matrix, print its transpose and flattened results.
* **Input Format:** The first line contains \(N\) and \(M\). The next \(N\) lines contain the space-separated elements.
* **Output Format:** Print the transposed array matrix first, followed by the 1D flattened array.

### Sample Input/Output
* **Sample Input:**
  ```text
  2 2
  1 2
  3 4
  ```
* **Sample Output:**
  ```text
  [[1 3]
   [2 4]]
  [1 2 3 4]
  ```

---

## Core Logic & Concepts

1. **`map()` for Integer Conversion:** We use `map(int, input().split())` to parse space-separated input strings into integers efficiently.
2. **Transposition (`.T`):** The `.T` property quickly reverses dimensions without copying data in memory.
3. **Flattening (`.flatten()`):** Collapses the array into a 1D copy of the continuous elements.

