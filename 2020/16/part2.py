import os

import ranges

cur_dir = os.path.dirname(os.path.abspath(__file__))


cur_ranges = set()
with open(f"{cur_dir}/input") as f:
    cur_line = f.readline()
    
    field_dict = {}
    while cur_line.strip() != "":
        field_name = cur_line.strip().split(": ")[0]
        field_ranges = set()
        field_ranges = ranges.extend_valid_ranges(field_ranges, cur_line.strip().split(": ")[1].split()[0])
        field_ranges = ranges.extend_valid_ranges(field_ranges, cur_line.strip().split(": ")[1].split()[2])
        field_dict[field_name] = field_ranges
        
        cur_ranges = ranges.extend_valid_ranges(cur_ranges, cur_line.strip().split(": ")[1].split()[0])
        cur_ranges = ranges.extend_valid_ranges(cur_ranges, cur_line.strip().split(": ")[1].split()[2])
        cur_line = f.readline()
    
    print(field_dict)
    
    f.readline()
    your_ticket = [int(x) for x in f.readline().strip().split(",")]

    print(your_ticket)
    
    f.readline()
    f.readline()
    cur_line = f.readline()
    
    valid_tickets = []
    while cur_line != "":
        new_ticket = [int(x) for x in cur_line.strip().split(",")]
        valid = True
        for x in new_ticket:
            if x not in cur_ranges:
                valid = False
        if valid:
            valid_tickets.append(new_ticket)
            
        cur_line = f.readline()
    
ticket_indices = [[x[i] for x in valid_tickets] for i in range(len(your_ticket))]
name_to_index_lookup = {}
for i, values in enumerate(ticket_indices):
    for field in field_dict:
        # if field in name_to_index_lookup:
        #     continue
        valid = True
        for x in values:
            if x not in field_dict[field]:
                valid = False
                break
        if valid:
            if field in name_to_index_lookup:
                name_to_index_lookup[field].add(i)
            else:
                name_to_index_lookup[field] = set([i])
print(name_to_index_lookup)

# Prune name_to_index_lookup
name_to_index_lookup_pruned = {}
while len(name_to_index_lookup_pruned) != len(your_ticket):
    for field in name_to_index_lookup:
        if len(name_to_index_lookup[field]) == 1:
            name_to_index_lookup_pruned[field] = name_to_index_lookup[field].pop()
    
    for field in name_to_index_lookup_pruned:
        val = name_to_index_lookup_pruned[field]
        for field_other in name_to_index_lookup:
            if val in name_to_index_lookup[field_other]:
                name_to_index_lookup[field_other].remove(val)
    
    print(name_to_index_lookup)
    print(name_to_index_lookup_pruned)
    
total_val = 1
for x in field_dict:
    if "departure" in x:
        total_val *= your_ticket[name_to_index_lookup_pruned[x]]
        
print(len(your_ticket))
        
print(total_val)
