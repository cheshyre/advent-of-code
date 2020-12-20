import os

import masked_memory_machine


cur_dir = os.path.dirname(os.path.abspath(__file__))

mymachine = masked_memory_machine.MaskedMemoryMachine2()

with open(f"{cur_dir}/input") as f:
    for line in f:
        if "mem" in line:
            addr = int(line.strip().split("] = ")[0].split("[")[1])
            val = int(line.strip().split("] = ")[1])
            mymachine.set_memory(addr, val)
        elif "mask" in line:
            mask = line.strip().split(" = ")[1]
            mymachine.set_mask(mask)
        else:
            print(f"Unknown command {line.strip()}")
            exit(-1)

sum_val = 0
for x in mymachine.memory:
    sum_val += mymachine.memory[x]
    
print(sum_val)
