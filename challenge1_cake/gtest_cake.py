def answer(s):
    strsize = len(s)
    factor_list = get_all_factors(strsize)
    best_fact = factor_crawl(s,factor_list)
    # String size divided by the smallest good factor = most slices
    num_slices = strsize/best_fact
    return num_slices
 
def get_all_factors(n):
    # This is a brute force factor list
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

def factor_crawl(mnmstring,factor_array):
    # Checks each factor. Splits the string into factor size chunks, smallest to largest
    # Stops if it makes it all the way through.
    for factor in factor_array:
        best_factor = True
        substr1 = mnmstring[:factor]
        beg_skip = factor
        end_skip = beg_skip + factor
        while end_skip <= len(mnmstring):
            substr2 = mnmstring[beg_skip:end_skip]
            if substr1 == substr2:
                beg_skip = end_skip
                end_skip += factor
            else:
                best_factor = False
                break
        if best_factor == True:
           true_best = factor
           break
    return true_best
