def generate_data(a):
    t = {'1': '0', '0': '1'}
    b = ''.join([t[x] for x in a[::-1]])
    # print(b)
    return '{}0{}'.format(a, b)

def calc_checksum(a):
    t = {'11': '1', '00': '1', '10': '0', '01': '0'}
    b = ''.join([t[a[i:i+2]] for i in range(0, len(a), 2)])
    return b

# Hardcoded input
disc_size = 272
data = '01110110101001000'

while len(data) < disc_size:
    data = generate_data(data)

checksum = data[:disc_size]

while len(checksum) % 2 == 0:
    checksum = calc_checksum(checksum)

print('The final checksum is {}.'.format(checksum))
