def do_step(last_called_dict, last_num_called, iteration):
    cur_num = 0
    if last_num_called in last_called_dict:
        cur_num = iteration - last_called_dict[last_num_called] - 1
    last_called_dict[last_num_called] = iteration - 1
    return last_called_dict, cur_num, iteration + 1
