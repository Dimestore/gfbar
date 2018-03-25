def answer(xs):
    # Set some variables. running_val is the running total
    running_val = None
    total_length = len(xs)
    neg_vals = []
    # Start the loop. Multiply all positive ints together, put the absolute value of the neg ints in an array
    for val in xs:
        if val > 0:
            if running_val is None:
                running_val = val
            else:
                running_val *= val
        elif val < 0:
            neg_vals.append(abs(val))
    # Begin the negative value evaluation. Start by sorting them to handle the odd number case easily.
    neg_vals.sort()
    add_neg = True
    nval_length = len(neg_vals)
    if nval_length <= 1:
        add_neg = False
    elif nval_length%2 != 0:
         del neg_vals[0]
    # Only include the values in the negative array if there are more than two.
    if add_neg == True:
        for n in neg_vals:
            if running_val is None:
                running_val = n
            else:
                running_val *= n
    # Final status check. If no positives and only one negative, return the negative
    if running_val is None and nval_length == 1 and total_length ==1:
        running_val = 0-neg_vals[0]
    # If our list had no positives but only 1 negative (i.e. [0,-4,0,0]) return 0
    elif running_val is None:
        running_val = 0
    # Else return the calculated value
    return str(running_val)
