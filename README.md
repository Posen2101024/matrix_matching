# Matrix Matching Algorithm

在二維矩陣 N\*M 中，匹配一個子矩陣 n\*m 的出現位置

時間複雜度 O(N\*M)

## Using Matrix Matching

- Sample code

```
from matrix_matching import MatrixMatching
import numpy as np
M, N, m, n = 1000, 1000, 100, 100
target = np.random.randint(2, size = (M, N))
matrix = np.random.randint(2, size = (m, n))
x, y = np.random.randint(M - m), np.random.randint(N - n)
target[x: x + m, y: y + n] = matrix
print(x, y)
print(MatrixMatching(target, matrix))
```

- Sample output

```
500 768
[500, 600, 768, 868]
```
