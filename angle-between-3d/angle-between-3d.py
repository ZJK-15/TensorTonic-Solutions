import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v_n = np.linalg.norm(v)
    w_n = np.linalg.norm(w)

    cs = np.dot(v,w)

    cosine = float(cs/(w_n * v_n))

    theta = np.arccos(cosine)
    return theta