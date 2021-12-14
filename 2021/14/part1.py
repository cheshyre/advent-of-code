import os


cur_dir = os.path.dirname(os.path.abspath(__file__))


def make_pairs(code):
    return [(code[i], code[i + 1]) for i in range(len(code) - 1)]


def make_new_code(code, rules):

    pairs = make_pairs(code)

    new_code = []
    for pair in pairs:

        new_code.append(pair[0])

        if pair in rules:
            new_code.append(rules[pair])

    new_code.append(pairs[-1][1])

    return new_code


with open(f"{cur_dir}/input") as f:
    code = [x for x in f.readline().strip()]
    _ = f.readline()

    line = f.readline()

    rules = {}
    while len(line) > 0:
        input = tuple([x for x in line.strip().split(" -> ")[0]])
        output = line.strip().split(" -> ")[1]

        rules[input] = output

        line = f.readline()


print(code)
print(rules)


for i in range(10):
    code = make_new_code(code, rules)

    # print("".join(code))

elems = list(set(code))

counts = [code.count(x) for x in elems]

counts = sorted(counts)

print(counts[-1] - counts[0])