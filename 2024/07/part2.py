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
    
    # Check concat possibilities
    tv_str = str(tv)
    vsl_str = str(vs[-1])
    cc_dim = len(vsl_str)
    if len(tv_str) > cc_dim and tv_str[-1 * cc_dim :] == vsl_str:
        rem = int(tv_str[: -1 * cc_dim])
        check_cc = check_operations(
            {
                "test_val": rem,
                "vals": vs[:-1],
            }
        )
        if check_cc:
            return True

    # Below is wrong
    # tv_str = str(tv)
    # for i in range(1, len(tv_str)):
    #     tvl = int(tv_str[:i])
    #     tvr = int(tv_str[i:])

    #     for j in range(1, len(vs)):

    #         vsl = vs[:j]
    #         vsr = vs[j:]

    #         if max(vsl) > tvl:
    #             continue

    #         if max(vsr) > tvr:
    #             continue

    #         if check_operations(
    #             {
    #                 "test_val": tvl,
    #                 "vals": vsl,
    #             }
    #         ) and check_operations(
    #             {
    #                 "test_val": tvr,
    #                 "vals": vsr,
    #             }
    #         ):
    #             return True

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
for i, vals in enumerate(input_vals):
    print(i)
    if check_operations(vals):
        count += vals["test_val"]
print(count)

