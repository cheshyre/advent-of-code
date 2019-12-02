instructions = []

with open('input') as f:
    for line in f:
        instructions.append(line.split())

class Computer:

    def __init__(self):
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        print(self.registers)

    def execute_instruction(self, instr):
        offset = 1
        if instr[0] == 'cpy':
            self.copy(instr[1], instr[2])
        elif instr[0] == 'inc':
            self.inc(instr[1])
        elif instr[0] == 'dec':
            self.dec(instr[1])
        elif instr[0] == 'jnz':
            offset = self.cond_jump(instr[1], instr[2])
        # print(' '.join([str(x) for x in instr]))
        # print(self.registers)
        return offset

    def copy(self, a, b):
        value = a
        if isinstance(a, str):
            value = self.registers[a]
        self.registers[b] = value

    def inc(self, a):
        self.registers[a] += 1

    def dec(self, a):
        self.registers[a] -= 1

    def cond_jump(self, a, b):
        value = a
        if isinstance(a, str):
            value = self.registers[a]
        if value != 0:
            return b
        else:
            return 1

for instr in instructions:
    for index in range(len(instr)):
        token = instr[index]
        try:
            token = int(token)
        except:
            pass
        instr[index] = token

i_counter = 0
count = 0
computer = Computer()

while i_counter < len(instructions):
    instr = instructions[i_counter]
    offset = computer.execute_instruction(instr)
    i_counter += offset
    count += 1
    if count % 1000 == 0:
        print('{} instructions executed. Currently at instruction {}.'.format(count, i_counter))

print('The final value of register a is {}.'.format(computer.registers['a']))
