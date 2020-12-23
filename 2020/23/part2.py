import os

import cups


# cur_dir = os.path.dirname(os.path.abspath(__file__))

# with open(f"{cur_dir}/input") as f:
#     pass

mycups = [int(x) for x in "583976241"]
min_val = min(mycups)
max_val = max(mycups)
mycups += list(range(max_val + 1, 1000001))
max_val = max(mycups)

cur_id = mycups[0]

mycups_dict = {x: cups.Cup(x) for x in mycups}
for i, x in enumerate(mycups[:-1]):
    mycups_dict[x].next = mycups_dict[mycups[i + 1]]
for x in mycups[-1:]:
    mycups_dict[x].next = mycups_dict[cur_id]
    
for _ in range(10000000):
    cur_id = cups.do_cup_rotation_new(mycups_dict, cur_id, min_val, max_val)
    
print(mycups_dict[1])
print(mycups_dict[1].next)
print(mycups_dict[1].next.next)
print(mycups_dict[1].next.name * mycups_dict[1].next.next.name)
