def get_all_sum_vals(prev_25):
    sum_vals = set()
    for x in prev_25:
        for y in prev_25:
            if x != y:
                sum_vals.add(x + y)
    return sum_vals


def identify_cont_set(target, arr):
    sum_val = 0
    for i, x in enumerate(arr):
        sum_val += x
        if sum_val == target:
            return i
        elif sum_val > target:
            return -1
    
    return -1
