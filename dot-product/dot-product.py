import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)

    if np.ndim(x) != np.ndim(y):
        return None
    return np.dot(x,y)
    pass