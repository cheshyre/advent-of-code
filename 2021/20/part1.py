import os


OFFSETS = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
BITREMAP = {
    ".": "0",
    "#": "1",
}


def print_image(image):
    for line in image:
        print(line)


def pad_image(image, char):
    dimx = len(image[0])

    new_image = []
    for _ in range(3):
        new_image.append(char * (dimx + 6))

    for row in image:
        new_image.append(char * 3 + row + char * 3)

    for _ in range(3):
        new_image.append(char * (dimx + 6))

    return new_image


def get_enhanced_pixel(image, row_i, col_i, algorithm):
    index_bin = "".join([BITREMAP[image[row_i + dr][col_i + dc]] for dr, dc in OFFSETS])

    return algorithm[int(index_bin, base=2)]


def enhance_image(image, algorithm, pad_char):

    padded_image = pad_image(image, pad_char)
    # print_image(padded_image)

    return [
        "".join(
            [
                get_enhanced_pixel(padded_image, row_i, col_i, algorithm)
                for col_i in range(1, len(padded_image[row_i]) - 1)
            ]
        )
        for row_i in range(1, len(padded_image) - 1)
    ]


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    lines = [line.strip() for line in f]

algorithm = lines[0]

swap = False
if algorithm[0] == "#":
    swap = True

swap_map = {
    ".": "#",
    "#": ".",
}

pad_char = "."

image = [line for line in lines[2:]]

# print_image(image)

image = enhance_image(image, algorithm, pad_char)
if swap:
    pad_char = swap_map[pad_char]

# print_image(image)

image = enhance_image(image, algorithm, pad_char)
if swap:
    pad_char = swap_map[pad_char]

# print_image(image)

print(sum([line.count("#") for line in image]))