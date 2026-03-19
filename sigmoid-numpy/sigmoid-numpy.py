import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    n = []
    x = np.asarray(x, dtype=float)
    if x.ndim == 0:
        return 1/(1+np.exp(-1*x))
    else:
        
        for i in x:
            n.append(1/(1+np.exp(-1*x)))      
            # Write code here
        n = np.asarray(n, dtype=float)
    return n