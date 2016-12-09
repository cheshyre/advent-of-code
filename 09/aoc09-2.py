from sys import argv

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

def parse_marker(s):
    s = s[1:-1]
    s = s.split('x')
    return int(s[0]), int(s[1])

def parse_and_get_length(l):
    if len(l) == 0:
        return 0
    length = 0
    marker_start = len(l.split('(')[0])
    marker_end = len(l.split(')')[0]) + 1
    length += marker_start
    if marker_start != len(l):
        x, y = parse_marker(l[marker_start:marker_end])
        length += y * parse_and_get_length(l[marker_end:marker_end + x])
        length += parse_and_get_length(l[marker_end + x:])
    return length


length = 0
with open(filename) as f:
    for line in f:
        line = line[:-1]
        length += parse_and_get_length(line)
        
print(length)
