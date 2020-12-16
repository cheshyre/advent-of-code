import os

import code_runner


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    commands = [x.strip() for x in f]

myrunner = code_runner.CodeRunner(commands)

for i in range(len(commands)):
    no_loop = myrunner.run_with_flipped_command(i)
    if no_loop:
        break

print(myrunner.acc)
    