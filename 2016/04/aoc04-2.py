from sys import argv

def sorting_key(a):
    value = a[1]
    value += (25 - (ord(a[0]) - 97))/26
    return -1*value

def shift_string(string, sector_id):
    a = []
    for x in string:
        val = ord(x) - 97
        val = (val + sector_id) % 26
        val += 97
        a.append(chr(val))

    return "".join(a)

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

with open(filename) as f:
    for line in f:
        a = line.split("-")
        name = "".join(a[:-1])
        b = a[-1].split("[")
        letters = b[1][:-2]
        sector_id = int(b[0])
        c = []
        for i in name:
            count = name.count(i)
            if (i, count) not in c:
                c.append((i, count))
        d = sorted(c, key=sorting_key)
        valid = True
        for i in range(len(letters)):
            if d[i][0] != letters[i]:
                valid = False
        if valid:
            e = []
            for x in a[:-1]:
                e.append(shift_string(x, sector_id))
            f = " ".join(e)
            print("{} - {}".format(f, sector_id))

# pipe into grep and search for "north"
