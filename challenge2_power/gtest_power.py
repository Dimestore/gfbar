def answer(xs):
    running_val = 1
    zero_count = 0
    neg_vals = []
    for val in xs:
        if val > 0:
            running_val *= val
        elif val < 0:
            neg_vals.append(abs(val))
        else:
            zero_count += 1
    neg_vals.sort()
    add_neg = True
    nval_length = len(neg_vals)
    if nval_length <= 1:
        add_neg = False
    elif nval_length%2 != 0:
        neg_vals[0] = 1
    if add_neg == True:
        for n in neg_vals:
            running_val *= n
    if len(xs) == zero_count:
        running_val = 0
    return str(running_val)
