import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if not np.isclose(sum(p), 1):
        raise ValueError("Sum of probabilities is not 1")
    sum1 = 0
    for i in range(len(p)):
        sum1 += x[i]*p[i]
    return sum1
