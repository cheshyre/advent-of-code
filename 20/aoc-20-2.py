from sys import argv

input_file = argv[1]

data = []
with open(input_file) as f:
    data = [[int(x) for x in line[:-1].split('-')] for line in f]

data.sort(key=lambda x: x[0])

# Remove range redundancy
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[j][0] < data[i][1]:
            data[j][0] = data[i][1] + 1

# Clean out useless ranges
data = [x for x in data if x[0] <= x[1]]

max_val = 0
max_ip = 4294967295
allowed_vals = 0
if data[0][0] != 0:
    allowed_vals += data[0][0]
for i in range(len(data) - 1):
    if data[i][1] > max_val:
        max_val = data[i][1]
    if data[i][1] < data[i + 1][0] - 1 and data[i][1] >= max_val:
        allowed_vals += data[i + 1][0] - data[i][1] - 1
allowed_vals += max_ip - max(max_val, data[-1][1])
print('There are {} allowed IPs.'.format(allowed_vals))
