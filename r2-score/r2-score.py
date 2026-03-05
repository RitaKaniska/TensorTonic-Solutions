import numpy as np

def sqr(x) -> float:
    return x * x

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_mean = sum(y_true) / len(y_true)
    tu = 0
    mau = 0
    for i in range(len(y_true)):
        tu += sqr(y_true[i] - y_pred[i])
        mau += sqr(y_true[i] - y_mean)
    if tu == 0:
        return 1
    if mau == 0: 
        return 0
    return 1 - tu / mau
        