import os

import code_runner


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    commands = [x.strip() for x in f]

myrunner = code_runner.CodeRunner(commands)
myrunner.run_until_repeat()
print(myrunner.acc)
    