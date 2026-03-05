import math

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    if num_bins == 1:
        return [1]
    max__ = max(values)
    min__ = min(values)
    w = (max__ - min__) / num_bins
    for i in range(len(values)):
        if w != 0:
            values[i] = min(math.floor((values[i] - min__) / w) , num_bins-1)
        else: values[i] = 0
    return values
    