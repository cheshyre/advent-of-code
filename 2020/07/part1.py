import os

import rules
import bags


cur_dir = os.path.dirname(os.path.abspath(__file__))

my_rules = {}
with open(f"{cur_dir}/input") as f:
    for line in f:
        new_rule = rules.Rule.from_string(line)
        my_rules[new_rule.name] = new_rule

gold_count = 0
for f in my_rules:
    if f == "shiny gold":
        continue
    my_bag = bags.Bag(f)
    
    while not my_bag.is_empty() and not my_bag.contains("shiny gold"):
        my_bag.unpack_once(my_rules)
        
    if my_bag.contains("shiny gold"):
        gold_count += 1

print(f"Gold count is {gold_count}")
    