from sys import argv

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

def l2m(l):
    if len(l) != 300:
        raise Exception("List length invalid: {}".format(len(l)))
    m = []
    for i in range(6):
        m.append(l[i * 50 : (i +1 ) * 50])
    return m

def m2l(m):
    l = []
    for i in range(len(m)):
        l += m[i]
    return l

def print_display(m):
    if len(m) != 6:
        raise Exception("Matrix length invalid: {}".format(len(m)))
    for i in range(len(m)):
        row = "".join([str(x) for x in m[i]]).replace('0', '.').replace('1', '#')
        print(row)

with open(filename) as f:
    display = [0] * 300
    display = l2m(display)
    for line in f:
        line = line[:-1]
        if line[0:4] == 'rect':
            x = int(line.split(" ")[-1].split('x')[0])
            y = int(line.split(" ")[-1].split('x')[1])
            for i in range(x):
                for j in range(y):
                    display[j][i] = 1
        elif 'rotate row' in line:
            line = line.replace('rotate row y=', '')
            row = int(line.split(' ')[0])
            offset = int(line.split(' ')[2])
            alt = []
            for i in range(len(display[row])):
                alt.append(display[row][(i - offset) % len(display[row])])
            for i in range(len(display[row])):
                display[row][i] = alt[i]
        elif 'rotate column' in line:
            line = line.replace('rotate column x=', '')
            col = int(line.split(' ')[0])
            offset = int(line.split(' ')[2])
            alt = []
            for i in range(len(display)):
                alt.append(display[i][col])
            for i in range(len(display)):
                display[i][col] = alt[(i - offset) % len(display)]
print_display(display)
print(m2l(display).count(1))





