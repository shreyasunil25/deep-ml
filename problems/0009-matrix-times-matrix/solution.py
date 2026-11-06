import numpy as np

def matrixmul(a: list[list[int|float]],
              b: list[list[int|float]]) -> list[list[int|float]]:

    n = len(a[0])
    m = len(b)

    if n != m:
        return -1

    p = len(a)
    q = len(b[0])

    c = np.zeros((p, q)).tolist()

    for i in range(p):
        for j in range(q):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c