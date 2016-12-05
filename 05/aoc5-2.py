from sys import argv
import hashlib

if len(argv) >= 2:
    puzzle_input = argv[1]
else:
    raise Exception("No puzzle input given.")

password = ""
mapping = {}

index = 0
for i in range(8):
    searching = True
    while searching:
        test_str = "{}{}".format(puzzle_input, index)
        m = hashlib.md5()
        m.update(bytearray(test_str, encoding='utf-8'))
        c = m.hexdigest()
        if str(c)[0:5] == "00000":
            position = str(c[5])
            character = str(c[6])
            if position not in mapping.keys() and int(position, 16) in range(8):
                mapping[position] = character
                searching = False
                print("{} - {}".format(test_str, c))
        index += 1

for i in range(8):
    password += mapping[str(i)]

print(password)
