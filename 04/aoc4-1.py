from sys import argv

def sorting_key(a):
    value = a[1]
    value += (25 - (ord(a[0]) - 97))/26
    return -1*value

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

sector_id_sum = 0
with open(filename) as f:
    for line in f:
        a = line.split("-")
        name = "".join(a[:-1])
        b = a[-1].split("[")
        letters = b[1][:-2]
        sector_id = b[0]
        c = []
        for a in name:
            count = name.count(a)
            if (a, count) not in c:
                c.append((a, count))
        d = sorted(c, key=sorting_key)
        valid = True
        for i in range(len(letters)):
            if d[i][0] != letters[i]:
                valid = False
        if valid:
            sector_id_sum += int(sector_id)

print(sector_id_sum)