import numpy as np
from scipy import stats
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    
    # Write code here

    median1 = np.median(x)
    mean1 = np.mean(x)
    mode1 = stats.mode(x,keepdims=False).mode
    return tuple([mean1,median1,mode1])