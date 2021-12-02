import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    commands = [(x.split()[0], int(x.split()[1])) for x in f]

def process_command(cmd, pos, depth, aim):
    if cmd[0] == "forward":
        return pos + cmd[1], depth + aim * cmd[1], aim
    if cmd[0] == "down":
        return pos, depth, aim + cmd[1]
    if cmd[0] == "up":
        return pos, depth, aim - cmd[1]
    raise Exception(f"invalid command: {cmd}")


pos = 0
depth = 0
aim = 0

for cmd in commands:
    pos, depth, aim = process_command(cmd, pos, depth, aim)
    
print(pos)
print(depth)
print(pos * depth)