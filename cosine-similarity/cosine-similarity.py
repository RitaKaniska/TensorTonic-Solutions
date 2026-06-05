import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    tu = float(np.sum(a * b))
    mau = np.linalg.norm(a) * np.linalg.norm(b)
    if mau != 0:
        return tu/mau
    else: return 0