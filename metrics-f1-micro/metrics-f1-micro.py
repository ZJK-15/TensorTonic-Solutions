import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    if np.ndim(y_pred) != np.ndim(y_true):
        return -1

    tp = 0

    for i in range(len(y_pred)):
        if y_pred[i] == y_true[i]:
            tp +=1


    return float(tp/len(y_pred))
    