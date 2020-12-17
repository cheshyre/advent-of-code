import os

import seating_plan


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    plan = [list(x.strip()) for x in f]
    
myplan = seating_plan.SeatingPlan(plan)
stable = False
looping = False
while not stable and not looping:
    stable, looping = myplan.do_step()

print(f"There are {myplan.count_occupied()} seats occupied.")
