def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    w = (max(values) - min(values))/num_bins
    if not w:
        return [0] * len(values)
    y = []
    for i in range(len(values)):
        y.append(min(int((values[i]-min(values))/w),num_bins - 1))

    return y