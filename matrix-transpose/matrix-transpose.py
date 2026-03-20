import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows = len(A)
    cols = len(A[0])

    B = [[0] * rows for _ in range(cols)]  # B has flipped dimensions: cols x rows

    for i in range(rows):
        for j in range(cols):
            B[j][i] = A[i][j]             # correct transpose assignment

    B = np.array(B)
    return B