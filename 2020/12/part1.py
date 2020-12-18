import os

import ship


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    commands = [x.strip() for x in f]

myship = ship.Ship()
for x in commands:
    myship.run_command(x)
    
print(f"The manhattan distance is {myship.manhattan_dist()}")
