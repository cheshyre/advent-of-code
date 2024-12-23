# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib


def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

input_lines = get_input_lines()

input_vals = [
    {
        "test_val": int(line.strip().split(":")[0]),
        "vals": [int(x) for x in line.strip().split(":")[1].split()],
    }
    for line in input_lines
]

def check_operations(
    vals
):
    tv = vals["test_val"]
    if tv < 0:
        return False
    vs = vals["vals"]
    if len(vs) == 1:
        return vs[0] == tv

    if tv % vs[-1] == 0:
        # Multiplication allowed
        check_mult = check_operations(
            {
                "test_val": tv // vs[-1],
                "vals": vs[:-1],
            }
        )
        if check_mult:
            return True
    
    # Otherwise addition is only hope
    check_add = check_operations(
        {
            "test_val": tv - vs[-1],
            "vals": vs[:-1],
        }
    )
    return check_add


count = 0
for vals in input_vals:
    if check_operations(vals):
        count += vals["test_val"]
print(count)

