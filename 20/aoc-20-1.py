from sys import argv

input_file = argv[1]

data = []
with open(input_file) as f:
    data = [[int(x) for x in line[:-1].split('-')] for line in f]

data.sort(key=lambda x: x[0])

val = None
max_val = 0
if data[0][0] != 0:
    print('Lowest allowed IP is 0.')
    exit()
for i in range(len(data) - 1):
    if data[i][1] > max_val:
        max_val = data[i][1]
    if data[i][1] < data[i + 1][0] - 1 and data[i][1] >= max_val:
        val = data[i][1] + 1
        break
if val == None:
    val = data[-1][1] + 1
print('Lowest allowed IP is {}.'.format(val))
