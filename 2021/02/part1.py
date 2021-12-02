import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    commands = [(x.split()[0], int(x.split()[1])) for x in f]

def process_command(cmd, pos, depth):
    if cmd[0] == "forward":
        return pos + cmd[1], depth
    if cmd[0] == "down":
        return pos, depth + cmd[1]
    if cmd[0] == "up":
        return pos, depth - cmd[1]
    raise Exception(f"invalid command: {cmd}")


pos = 0
depth = 0

for cmd in commands:
    pos, depth = process_command(cmd, pos, depth)
    
print(pos)
print(depth)
print(pos * depth)