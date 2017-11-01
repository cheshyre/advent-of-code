from sys import argv

start_row = argv[1]
num_rows = int(argv[2])
row_length = len(start_row)

def get_prev_row_data(string, index, row_length):
    if index == 0:
        return '.' + string[0:2]
    elif index == row_length - 1:
        return string[row_length - 2:row_length] + '.'
    else:
        return string[index - 1:index + 2]

safe_states_count = start_row.count('.')
previous_row = start_row
for i in range(1, num_rows):
    new_row = ''
    for j in range(row_length):
        data = get_prev_row_data(previous_row, j, row_length)
        if data[0] != data[2]:
            new_row += '^'
        else:
            new_row += '.'
    safe_states_count += new_row.count('.')
    previous_row = new_row

print('There are {} safe states in the {} row space.'.format(safe_states_count, num_rows))
