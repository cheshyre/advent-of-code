import os


cur_dir = os.path.dirname(os.path.abspath(__file__))


def make_pairs(code):
    return [(code[i], code[i + 1]) for i in range(len(code) - 1)]


def make_counts(code, end):

    counts = {}
    for p, q in code:
        if p in counts:
            counts[p] += code[(p, q)]
        else:
            counts[p] = code[(p, q)]
    if end in counts:
        counts[end] += 1
    else:
        counts[end] = 1
    return counts


def make_new_code(code, rules):

    new_code = {}
    for pair in code:

        pair_count = code[pair]

        if pair in rules:
            p1, p2 = rules[pair]
            if p1 in new_code:
                new_code[p1] += pair_count
            else:
                new_code[p1] = pair_count
            if p2 in new_code:
                new_code[p2] += pair_count
            else:
                new_code[p2] = pair_count

        else:
            if pair in new_code:
                new_code[pair] += pair_count
            else:
                new_code[pair] = pair_count

    return new_code


with open(f"{cur_dir}/input") as f:
    code = [x for x in f.readline().strip()]
    _ = f.readline()

    line = f.readline()

    rules = {}
    while len(line) > 0:
        input = tuple([x for x in line.strip().split(" -> ")[0]])
        output = line.strip().split(" -> ")[1]

        rules[input] = [(input[0], output), (output, input[1])]

        line = f.readline()

end = code[-1]

code_pairs = make_pairs(code)
code = {x: code_pairs.count(x) for x in code_pairs}
print(code)
print(rules)


for i in range(40):
    print(code)
    code = make_new_code(code, rules)

    # print("".join(code))

counts = make_counts(code, end)

counts = [counts[x] for x in counts]

counts = sorted(counts)

print(counts[-1] - counts[0])