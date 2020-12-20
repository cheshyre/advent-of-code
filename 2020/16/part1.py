import os

import ranges

cur_dir = os.path.dirname(os.path.abspath(__file__))


cur_ranges = set()
with open(f"{cur_dir}/input") as f:
    cur_line = f.readline()
    
    while cur_line.strip() != "":
        cur_ranges = ranges.extend_valid_ranges(cur_ranges, cur_line.strip().split(": ")[1].split()[0])
        cur_ranges = ranges.extend_valid_ranges(cur_ranges, cur_line.strip().split(": ")[1].split()[2])
        cur_line = f.readline()
    
    print(cur_ranges)
    
    f.readline()
    your_ticket = [int(x) for x in f.readline().strip().split(",")]

    print(your_ticket)
    
    f.readline()
    f.readline()
    cur_line = f.readline()
    
    failed_tickets = 0
    while cur_line != "":
        new_ticket = [int(x) for x in cur_line.strip().split(",")]
        for x in new_ticket:
            if x not in cur_ranges:
                failed_tickets += x
        cur_line = f.readline()
                
print(failed_tickets)
        
        

