import os


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    arrival_time = int(f.readline().strip())
    buses = [int(x) for x in f.readline().strip().split(',') if x != "x"]
    
print(arrival_time)
min_wait = buses[0] - arrival_time % buses[0]
min_bus = buses[0]
if min_wait == min_bus:
    min_wait = 0
for bus in buses:
    wait = bus - arrival_time % bus
    if wait == bus:
        wait = 0
    if wait < min_wait:
        min_wait = wait
        min_bus = bus
        
print(f"You need to wait {min_wait} minutes with bus {min_bus}.")
print(f"This gives the product {min_wait * min_bus}.")
    
