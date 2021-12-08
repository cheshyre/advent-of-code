import os

digit_decoder = {
    "25": 1,
    "02346": 2,
    "02356": 3,
    "1235": 4,
    "01356": 5,
    "013456": 6,
    "025": 7,
    "0123456": 8,
    "012356": 9,
    "012456": 0,
}


def apply_mapping(values, mapping):
    digits = []
    for x in values:
        digit = "".join(sorted([mapping[y] for y in x]))
        digits.append(digit)
    return digits


def is_mapping_valid(inputs, mapping):
    digits = apply_mapping(inputs, mapping)
    for x in digits:
        if x not in digit_decoder:
            return False
    return True


def decode_digits(digits):
    return [digit_decoder[x] for x in digits]


def determine_possible_mappings(inputs):
    one = set()
    four = set()
    seven = set()
    eight = set()
    for x in inputs:
        if len(x) == 2:
            one = {y for y in x}
        elif len(x) == 4:
            four = {y for y in x}
        elif len(x) == 3:
            seven = {y for y in x}
        elif len(x) == 7:
            eight = {y for y in x}
    # print(one)
    # print(four)
    # print(seven)
    # print(eight)
    seg0 = list(seven.difference(one))[0]
    seg13 = list(four.difference(one))
    seg25 = list(one)
    seg46 = list(eight.difference(seven).difference(four))

    mappings = []
    for seg1, seg3 in [(seg13[0], seg13[1]), (seg13[1], seg13[0])]:
        for seg2, seg5 in [(seg25[0], seg25[1]), (seg25[1], seg25[0])]:
            for seg4, seg6 in [(seg46[0], seg46[1]), (seg46[1], seg46[0])]:
                mappings.append(
                    {
                        seg0: "0",
                        seg1: "1",
                        seg2: "2",
                        seg3: "3",
                        seg4: "4",
                        seg5: "5",
                        seg6: "6",
                    }
                )

    return mappings


cur_dir = os.path.dirname(os.path.abspath(__file__))


values = []
with open(f"{cur_dir}/input") as f:
    for line in f:
        inputs = line.strip().split(" | ")[0].split()
        outputs = line.strip().split(" | ")[1].split()
        values.append((inputs, outputs))

sum_val = 0
for input, output in values:
    print(input)
    mappings = determine_possible_mappings(input)
    for mapping in mappings:
        # print(mapping)
        # print(input)
        # print(apply_mapping(input, mapping))
        if is_mapping_valid(input, mapping):
            val = int(
                "".join([str(x) for x in decode_digits(apply_mapping(output, mapping))])
            )
            print(val)
            sum_val += val

print(sum_val)
