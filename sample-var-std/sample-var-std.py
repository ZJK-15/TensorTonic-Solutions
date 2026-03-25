import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    mean = float(sum(x)/len(x))
    sum1 = 0
    for i in range(len(x)):
        sum1 += (x[i] - mean)**2
    sum1 /= len(x) - 1
    return [sum1,np.sqrt(sum1)]
    pass