def extend_valid_ranges(cur_ranges, new_range):
    min_val = int(new_range.split("-")[0])
    max_val = int(new_range.split("-")[1])
    for x in range(min_val, max_val + 1):
        cur_ranges.add(x)
        
    return cur_ranges
