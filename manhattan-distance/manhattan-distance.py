import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    distance = 0

    if np.ndim(x) != np.ndim(y):
        return -1

    for i in range(len(x)):
        distance += np.abs(x[i] - y[i])

    return int(distance)