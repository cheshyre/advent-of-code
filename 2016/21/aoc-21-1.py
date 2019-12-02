from sys import argv

filename = argv[1]

with open(filename) as f:
    instructions = [line[:-1] for line in f]

def swap_pos(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    return arr

def swap_letter(arr, a, b):
    index1 = arr.index(a)
    index2 = arr.index(b)
    return swap_pos(arr, index1, index2)

def rot_right(arr, n):
    n = n % len(arr)
    return arr[-1 * n:] + arr[:-1 * n]

def rot_left(arr, n):
    n = n % len(arr)
    return arr[n:] + arr[:n]

def rot_letter(arr, a):
    index = arr.index(a)
    if index >= 4:
        index += 1
    index += 1
    return rot_right(arr, index % len(arr))

def reverse(arr, x, y):
    if x == 0:
        seg1 = []
    else:
        seg1 = arr[:x]
    if y == len(arr) - 1:
        seg2 = []
    else:
        seg2 = arr[y+1:]
    mid = arr[x:y+1][::-1]
    return seg1 + mid + seg2

def mov(arr, x, y):
    a = arr.pop(x)
    arr[y:y] = [a]
    return arr

initial_string = 'abcdefgh'
password = [x for x in initial_string]

for x in instructions:
    tokens = x.split()
    if tokens[0] == 'swap' and tokens[1] == 'position':
        password = swap_pos(password, int(tokens[2]), int(tokens[5]))
    elif tokens[0] == 'swap' and tokens[1] == 'letter':
        password = swap_letter(password, tokens[2], tokens[5])
    elif tokens[0] == 'rotate' and tokens[1] == 'right':
        password = rot_right(password, int(tokens[2]))
    elif tokens[0] == 'rotate' and tokens[1] == 'left':
        password = rot_left(password, int(tokens[2]))
    elif tokens[0] == 'rotate':
        password = rot_letter(password, tokens[-1])
    elif tokens[0] == 'reverse':
        password = reverse(password, int(tokens[2]), int(tokens[4]))
    else:
        password = mov(password, int(tokens[2]), int(tokens[5]))

print('The scrambled password is {}.'.format(''.join(password)))
