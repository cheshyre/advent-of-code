# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib
import re


def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

def parse_mul_command(mul_cmd):
    l_arg = int(mul_cmd.split("(")[1].split(",")[0])
    r_arg = int(mul_cmd.split(",")[1].split(")")[0])

    return l_arg * r_arg


def get_active_parts(row):
    do_statements = row.split("do()")
    return [x.split("don't()")[0] for x in do_statements]

    
lines = get_input_lines()
one_big_line = "".join(lines)

total = 0
for row in [one_big_line]:
    for active_part in get_active_parts(row):
        matches = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", active_part)

        for match in matches:
            total += parse_mul_command(match)

print(total)
