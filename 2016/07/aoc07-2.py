from sys import argv

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

def swap(s):
    if len(s) != 3:
        raise Exception("Invalid string given: {}".format(s))
    return "".join([s[1], s[0], s[1]])

count = 0
with open(filename) as f:
    for line in f:
        line = line[:-1]
        valid = False
        in_hypernet = False
        external = set()
        internal = set()
        for i in range(len(line) - 2):
            if not in_hypernet and line[i] == '[':
                in_hypernet = True
            elif in_hypernet and line[i] == ']':
                in_hypernet = False
            if line[i] == line[i + 2] and line[i] != line[i + 1]:
                if in_hypernet:
                    internal.add(line[i:i + 3])
                else:
                    external.add(line[i:i + 3])
        for i in internal:
            if swap(i) in external:
                valid = True
                break
        if valid:
            count += 1

print(count)
