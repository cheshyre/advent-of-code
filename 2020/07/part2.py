import os

import rules
import bags


cur_dir = os.path.dirname(os.path.abspath(__file__))

my_rules = {}
with open(f"{cur_dir}/input") as f:
    for line in f:
        new_rule = rules.Rule.from_string(line)
        my_rules[new_rule.name] = new_rule

gold_bag = bags.Bag("shiny gold")
while not gold_bag.is_empty():
    gold_bag.unpack_once(my_rules)
    
print(f"A shiny gold bag contains {gold_bag.contained_bags} bags.")
