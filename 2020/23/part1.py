import os

import cups


# cur_dir = os.path.dirname(os.path.abspath(__file__))

# with open(f"{cur_dir}/input") as f:
#     pass

mycups = [int(x) for x in "583976241"]
min_val = min(mycups)
max_val = max(mycups)

print(mycups)
for _ in range(100):
    mycups = cups.do_cup_rotation(mycups, min_val, max_val)
    print(mycups)

one_index = mycups.index(1)
new_cups = mycups[one_index:] + mycups[:one_index]

print("".join([str(x) for x in new_cups]))
