import os
import re

import rule


cur_dir = os.path.dirname(os.path.abspath(__file__))

match_count = 0
with open(f"{cur_dir}/input") as f:
    cur_line = f.readline()
    rules_lookup = {}
    while cur_line.strip() != "":
        rule_name, cur_rule = rule.parse_rule_from_line(cur_line)
        rules_lookup[rule_name] = cur_rule
        cur_line = f.readline()

    success, rules_lookup = rules_lookup["42"].attempt_to_make_literal(rules_lookup)
    success, rules_lookup = rules_lookup["31"].attempt_to_make_literal(rules_lookup)
    print(rules_lookup["42"])
    print(rules_lookup["31"])
    
    cur_line = f.readline()
    while cur_line != "":
        if rule.check_string(cur_line.strip(), rules_lookup["42"].matched_str_list, rules_lookup["31"].matched_str_list):
            match_count += 1
        cur_line = f.readline()
        
print(f"{match_count} strings were matched.")
