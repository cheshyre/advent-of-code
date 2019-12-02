from sys import argv

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

def parse(s, in_hypernet):
    if len(s) != 4:
        raise Exception("Invalid string given: {}".format(s))
    if s[0:2] == s[-1:-3:-1] and s[0] != s[1]:
        if in_hypernet:
            return -1
        else:
            return 1
    else:
        return 0

count = 0
with open(filename) as f:
    for line in f:
        line = line[:-1]
        valid = False
        in_hypernet = False
        for i in range(len(line) - 3):
            if not in_hypernet and line[i] == '[':
                in_hypernet = True
            elif in_hypernet and line[i] == ']':
                in_hypernet = False
            a = parse(line[i:i + 4], in_hypernet)
            if a == -1:
                valid = False
                break
            elif a == 1:
                valid = True
        if valid:
            count += 1

print(count)
