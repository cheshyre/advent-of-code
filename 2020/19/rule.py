def check_string(some_string, valid_strings_start, valid_strings_end):
    end_matches = 0
    start_matches = 0
    unit_len = len(valid_strings_start[0])
    if len(some_string) % unit_len != 0:
        return False
    if some_string[:unit_len] in valid_strings_start:
        start_matches += 1
    else:
        return False
    if some_string[-1 * unit_len :] in valid_strings_end:
        end_matches += 1
    else:
        return False
    checking_end = False
    for i in range(unit_len, len(some_string) - unit_len, unit_len):
        substr = some_string[i: i+unit_len]
        if not checking_end:
            if substr in valid_strings_start:
                start_matches += 1
            else:
                checking_end = True
        if checking_end:
            if substr in valid_strings_end:
                end_matches += 1
            else:
                return False
    return start_matches > end_matches


class LiteralRule:
    
    def __init__(self, name, matched_str_list):
        self.name = name
        
        self.type = "literal"
        
        self.matched_str_list = sorted(matched_str_list)
        
    def match(self, some_string, rule_lookup):
        # print(some_string)
        for x in self.matched_str_list:
            if some_string[:len(x)] == x:
                return True, some_string[len(x):]
        return False, some_string
    
    def complete_match(self, some_string, rule_lookup):
        matched, rem_string = self.match(some_string, rule_lookup)
        if rem_string != "":
            return False
        return matched
    
    def __repr__(self):
        return self.name + ": " + "|".join(self.matched_str_list)
    
    def as_regex(self):
        return "|".join(self.matched_str_list)
        

class RecursiveRule:
    
    def __init__(self, name, subrules):
        self.name = name
        self.type = "recursive"
        
        self.subrules = subrules
        
    def match(self, some_string, rule_lookup):
        
        # print(some_string)
        cur_string = some_string
        
        for rule_set in self.subrules:
            for rule in rule_set:
                # print(f"Before partial match: {cur_string}")
                matched, cur_string = rule_lookup[rule].match(cur_string, rule_lookup)
                # if matched:
                #     print(f"After partial match: {cur_string}")
                # else:
                #     print("Did not match")
                if not matched:
                    cur_string = some_string
                    break
            if matched:
                # print(f"Matched rule set: {rule_set}")
                return True, cur_string
        return False, some_string
    
    def complete_match(self, some_string, rule_lookup):
        matched, rem_string = self.match(some_string, rule_lookup)
        if matched and rem_string != "":
            # print(f"Remaining string: {rem_string}")
            return False
        return matched
    
    def attempt_to_make_literal(self, rule_lookup):
        success_for_sub_rules = True
        for rule_set in self.subrules:
            for rule in rule_set:
                if rule == self.name:
                    success_for_sub_rules = False
                    continue
                if rule_lookup[rule].type == "recursive":
                    success, rule_lookup = rule_lookup[rule].attempt_to_make_literal(rule_lookup)
                    success_for_sub_rules = success_for_sub_rules and success
        
        if not success_for_sub_rules:
            return False, rule_lookup
        
        possible_matches = []
        for rule_set in self.subrules:
            cur_matches = rule_lookup[rule_set[0]].matched_str_list
            next_matches = []
            for rule in rule_set[1:]:
                for word2 in rule_lookup[rule].matched_str_list:
                    for word1 in cur_matches:
                        new_word = f"{word1}{word2}"
                        if new_word not in next_matches:
                            next_matches.append(new_word)
                cur_matches = next_matches
                next_matches = []
            possible_matches += cur_matches
        new_rule = LiteralRule(self.name, possible_matches)
        rule_lookup[self.name] = new_rule
        return True, rule_lookup
    
    
class LoopingRuleSingle:
    
    def __init__(self, name, looped_literal_sub_rule):
        self.name = name
        self.subrule = looped_literal_sub_rule
        
    def match(self, some_string, rule_lookup):
        matched, rem_string = self.subrule.match(some_string, rule_lookup)
        while matched and rem_string != "":
            matched, rem_string = self.subrule.match(rem_string, rule_lookup)
        return matched, rem_string
    
    
class LoopingRuleDoubleCustom:
    
    def __init__(self, name, looped_literal_sub_rule1, looped_literal_sub_rule2):
        self.name = name
        self.subrule1 = looped_literal_sub_rule1
        self.subrule2 = looped_literal_sub_rule2
        
    def match(self, some_string, rule_lookup):
        print(some_string)
        rule_1_match_counts = 0
        rule_2_match_counts = 0
        matched, rem_string = self.subrule1.match(some_string, rule_lookup)
        rule_1_match_counts += 1
        if not matched:
            return False, some_string
        while matched and rem_string != "":
            matched, rem_string = self.subrule1.match(rem_string, rule_lookup)
            rule_1_match_counts += 1
        matched, rem_string = self.subrule2.match(rem_string, rule_lookup)
        rule_2_match_counts += 1
        if not matched:
            return False, some_string
        while matched and rem_string != "":
            matched, rem_string = self.subrule2.match(rem_string, rule_lookup)
            rule_2_match_counts += 1
        print(rule_1_match_counts)
        print(rule_2_match_counts)
        if not matched or rule_2_match_counts >= rule_1_match_counts:
            return False, some_string
        return matched, rem_string
    
    def complete_match(self, some_string, rule_lookup):
        matched, rem_string = self.match(some_string, rule_lookup)
        if matched and rem_string != "":
            # print(f"Remaining string: {rem_string}")
            return False
        return matched
    
    
class LoopingRuleDouble:
    
    def __init__(self, name, looped_literal_sub_rule1, looped_literal_sub_rule2):
        self.name = name
        self.subrule1 = looped_literal_sub_rule1
        self.subrule2 = looped_literal_sub_rule2
        # We need to worry about rule lengths for easy processing
        self.rule1_len = len(looped_literal_sub_rule1.matched_str_list[0])
        self.rule2_len = len(looped_literal_sub_rule2.matched_str_list[0])
        
    def match(self, some_string, rule_lookup):
        if len(some_string) % (self.rule1_len + self.rule2_len) != 0:
            return False, some_string
        iterations = len(some_string) // (self.rule1_len + self.rule2_len)
        some_string_substr1 = some_string[:iterations * self.rule1_len]
        some_string_substr2 = some_string[iterations * self.rule1_len:]
        matched, rem_string = self.subrule1.match(some_string_substr1, rule_lookup)
        while matched and rem_string != "":
            matched, rem_string = self.subrule1.match(rem_string, rule_lookup)
        if not matched:
            return matched, some_string
        matched, rem_string = self.subrule2.match(some_string_substr2, rule_lookup)
        while matched and rem_string != "":
            matched, rem_string = self.subrule2.match(rem_string, rule_lookup)
        if not matched:
            return matched, some_string
        return matched, rem_string


def parse_rule_from_line(line):
    line = line.strip()
    line_name = line.split(": ")[0]
    line_rules = line.split(": ")[1]
    if "\"" in line_rules:
        return line_name, LiteralRule(line_name, [line_rules[1:-1]])
    recursive_rules = [[x for x in rule_set.split()] for rule_set in line_rules.split(" | ")]
    return line_name, RecursiveRule(line_name, recursive_rules)
