from sys import argv

def sorting_key(a):
    return a[1]

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

counts = []
indexes = []

final_string = ""

with open(filename) as f:
    c = f.readline()[:-1]
    str_len = len(c)
    for i in range(str_len):
        counts.append([(c[i], 1)])
        indexes.append({})
        indexes[i][c[i]] = 0
    c = f.readline()[:-1]
    while c != "":
        for i in range(str_len):
            if c[i] in indexes[i]:
                counts[i][indexes[i][c[i]]] = (c[i], counts[i][indexes[i][c[i]]][1] + 1)
            else:
                indexes[i][c[i]] = len(counts[i])
                counts[i].append((c[i], 1))
        c = f.readline()[:-1]
    for i in range(str_len):
        array = sorted(counts[i], key=sorting_key)
        final_string += array[0][0]

print(final_string)
