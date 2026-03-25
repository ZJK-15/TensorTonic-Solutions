import numpy as np

def tanh(x):
    x = np.array(x, dtype=float)   # Convert safely to NumPy array
    return np.tanh(x)              # Built-in handles everything