import os


cur_dir = os.path.dirname(os.path.abspath(__file__))

num_questions = 0
with open(f"{cur_dir}/input") as f:
    cur_group = set()
    initialized = False
    for line in f:
        if line == "\n":
            num_questions += len(cur_group)
            cur_group = set()
            initialized = False
        else:
            new_member_in_group = {x for x in line.strip()}
            if initialized:
                cur_group = cur_group.intersection(new_member_in_group)
            else:
                cur_group = new_member_in_group
                initialized = True
            
print(f"{num_questions} total questions were asked")
