from sys import argv

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

def parse_marker(s):
    s = s[1:-1]
    s = s.split('x')
    return int(s[0]), int(s[1])

with open(filename) as f:
    for line in f:
        line = line[:-1]
        marker_start = -1
        marker_end = -1
        i = 0
        final_str = ''
        while i < len(line):
            if marker_start == -1 and line[i] == '(':
                marker_start = i
                i += 1
            elif marker_start == -1:
                final_str += line[i]
                i += 1
            elif marker_start != -1 and line[i] != ')':
                i += 1
            else:
                marker_end = i + 1
                x, y = parse_marker(line[marker_start:marker_end])
                iter_str = line[marker_end:marker_end + x]
                i += x + 1
                for z in range(y):
                    final_str += iter_str
                marker_start = -1
                marker_end = -1
print(final_str)
print(len(final_str))
