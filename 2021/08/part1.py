import os


cur_dir = os.path.dirname(os.path.abspath(__file__))


values = []
with open(f"{cur_dir}/input") as f:
    for line in f:
        inputs = line.strip().split(" | ")[0].split()
        outputs = line.strip().split(" | ")[1].split()
        values.append((inputs, outputs))

count_1 = 0
count_4 = 0
count_7 = 0
count_8 = 0

for input, output in values:
    for x in output:
        if len(x) == 2:
            count_1 += 1
        elif len(x) == 4:
            count_4 += 1
        elif len(x) == 3:
            count_7 += 1
        elif len(x) == 7:
            count_8 += 1

print(count_1 + count_4 + count_7 + count_8)
