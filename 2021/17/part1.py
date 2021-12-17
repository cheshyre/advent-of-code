import os


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    pass

print(sum([x for x in range(99)]))
