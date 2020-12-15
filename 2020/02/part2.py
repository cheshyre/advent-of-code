import os

import password_rules


cur_dir = os.path.dirname(os.path.abspath(__file__))

num_valid = 0
with open(f"{cur_dir}/input") as f:
    for line in f:
        rule = password_rules.RuleType2.from_string(line.strip().split(": ")[0])
        test_string = line.strip().split(": ")[1]
        if rule.check_string(test_string):
            num_valid += 1
            
print(f"{num_valid} passwords are valid")
