def robust_scaling(values):
    n = len(values)
    sorted_vals = sorted(values)  # only for computing stats

    def median(lst):
        m = len(lst)
        mid = m // 2
        if m % 2 == 1:
            return float(lst[mid])
        else:
            return (lst[mid - 1] + lst[mid]) / 2.0

    if n == 1:
        return [0.0]

    med = median(sorted_vals)

    mid = n // 2
    lower_half = sorted_vals[:mid]
    upper_half = sorted_vals[mid + 1:] if n % 2 == 1 else sorted_vals[mid:]

    q1 = median(lower_half)
    q3 = median(upper_half)

    iqr = q3 - q1

    if iqr == 0:
        return [float(v - med) for v in values]  # ✅ original order

    return [(v - med) / iqr for v in values]  # ✅ original order