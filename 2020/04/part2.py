import os

import passport


cur_dir = os.path.dirname(os.path.abspath(__file__))

num_valid = 0
with open(f"{cur_dir}/input") as f:
    cur_passport = {}
    for line in f:
        if line == "\n":
            if passport.check_passport_validity_full(cur_passport):
                num_valid += 1
            cur_passport = {}
        else:
            cur_passport = passport.merge_dict(
                cur_passport,
                passport.line_to_dict(line)
            )
            
print(f"{num_valid} passports were valid")
