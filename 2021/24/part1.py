import functools
import os
from typing import Sequence, Union, List

cur_dir = os.path.dirname(os.path.abspath(__file__))

NUMBERS = [str(x) for x in range(10)]


class ALU:
    def __init__(
        self, commands: Sequence[Sequence[Union[int, str]]], inputs: Sequence[int]
    ) -> None:
        self.commands = commands
        self.instr_index = 0
        self.inputs = inputs
        self.input_index = 0
        self.registers = {
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }

    def eval_input(self, register: str) -> None:
        self.registers[register] = self.inputs[self.input_index]
        self.input_index += 1

    def get_value(self, val: Union[int, str]) -> int:
        if isinstance(val, int):
            return val
        return self.registers[val]

    def eval_add(self, register: str, val: Union[int, str]) -> None:
        self.registers[register] += self.get_value(val)

    def eval_mul(self, register: str, val: Union[int, str]) -> None:
        self.registers[register] *= self.get_value(val)

    def eval_div(self, register: str, val: Union[int, str]) -> None:
        b = self.get_value(val)
        if b == 0:
            raise Exception("Attempted division by 0.")
        result = self.registers[register] // b
        # Handle different behavior when dealing with negative integer division
        if result < 0:
            result += 1
        self.registers[register] = result

    def eval_mod(self, register: str, val: Union[int, str]) -> None:
        b = self.get_value(val)
        a = self.registers[register]
        if a < 0:
            raise Exception("Attempted modulo of a negative number.")
        if b <= 0:
            raise Exception("Attempted modulo by 0 or negative number.")
        self.registers[register] = a % b

    def eval_eql(self, register: str, val: Union[int, str]) -> None:
        if self.registers[register] == self.get_value(val):
            self.registers[register] = 1
        else:
            self.registers[register] = 0

    def eval_instruction(self) -> None:
        cur_instr = self.commands[self.instr_index]
        command = cur_instr[0]

        if command == "inp":
            self.eval_input(cur_instr[1])
        elif command == "add":
            self.eval_add(cur_instr[1], cur_instr[2])
        elif command == "mul":
            self.eval_mul(cur_instr[1], cur_instr[2])
        elif command == "div":
            self.eval_div(cur_instr[1], cur_instr[2])
        elif command == "mod":
            self.eval_mod(cur_instr[1], cur_instr[2])
        elif command == "eql":
            self.eval_eql(cur_instr[1], cur_instr[2])

        self.instr_index += 1

    def run_program(self) -> None:
        while self.instr_index < len(self.commands):
            self.eval_instruction()


def parse_input_line(line: str) -> List[Union[int, str]]:
    command = [x for x in line.strip().split()]
    try:
        command[-1] = int(command[-1])
    except ValueError:
        pass
    return command


@functools.lru_cache(maxsize=None)
def load_program(min_ln, max_ln):
    with open(f"{cur_dir}/input") as f:
        lines = [line for line in f]
    program = [parse_input_line(line) for line in lines[min_ln:max_ln]]
    return program


@functools.lru_cache(maxsize=None)
def evaluate_program(val: int, z: int, min_ln: int, max_ln: int) -> int:
    program = load_program(min_ln, max_ln)

    alu = ALU(program, [val])
    alu.registers["z"] = z
    alu.run_program()
    return alu.registers["z"]


def evaluate_program_no_mem(val: int, z: int, min_ln: int, max_ln: int) -> int:
    program = load_program(min_ln, max_ln)

    alu = ALU(program, [val])
    alu.registers["z"] = z
    alu.run_program()
    return alu.registers["z"]


# with open(f"{cur_dir}/sample_input") as f:
#     program = [parse_input_line(line) for line in f]


# for x in range(-20, 20):
#     print(x)
#     alu = ALU(program, [x])
#     alu.run_program()
#     print(alu.registers["x"])


# with open(f"{cur_dir}/sample_input2") as f:
#     program = [parse_input_line(line) for line in f]


# for x in range(-10, 10):
#     for y in [2 * x, 3 * x, 4 * x]:
#         print((x, y))
#         alu = ALU(program, [x, y])
#         alu.run_program()
#         print(alu.registers["z"])


# with open(f"{cur_dir}/sample_input3") as f:
#     program = [parse_input_line(line) for line in f]


# for x in range(0, 16):
#     print(x)
#     alu = ALU(program, [x])
#     alu.run_program()
#     print(
#         (alu.registers["w"], alu.registers["x"], alu.registers["y"], alu.registers["z"])
#     )

with open(f"{cur_dir}/input") as f:
    lines = [line for line in f]

starts = [i for i, x in enumerate(lines) if "inp" in x]
ends = [i for i in starts[1:]] + [len(lines)]
z_domains = [[0]] + [[]] * (len(starts) - 1)
z_ranges = [set()] * (len(starts) - 1) + [set([0])]

print(starts)
print(ends)

for i in range(len(starts) // 2):
    min_ln = starts[i]
    max_ln = ends[i]
    z_domain = z_domains[i]

    z_range = list(
        {
            evaluate_program(val, z, min_ln, max_ln)
            for val in range(1, 10)
            for z in z_domain
        }
    )

    print(z_range)

    z_ranges[i] = set(z_range)
    z_domains[i + 1] = z_range
    print(len(z_range))

for i in range(13, 6, -1):
    min_ln = starts[i]
    max_ln = ends[i]

    z_range = {
        z
        for val in range(1, 10)
        for z in range(20000)
        if evaluate_program(val, z, min_ln, max_ln) in z_ranges[i]
    }
    z_ranges[i - 1] = z_range
    z_domains[i] = list(z_range)
    print(max(z_range))
    print(len(z_range))


def get_valid_model_number(i, target) -> List[str]:
    min_ln = starts[i]
    max_ln = ends[i]
    z_domain = z_domains[i]
    solutions = [
        (val, z)
        for val in range(1, 10)
        for z in z_domain
        if evaluate_program(val, z, min_ln, max_ln) == target
    ]
    print(i)
    # print(target)
    # print(solutions)
    if i == 0:
        return [str(x) for x, _ in solutions]
    else:
        model_numbers = []
        for val, z in solutions:
            for partial_mn in get_valid_model_number(i - 1, z):
                model_numbers.append(partial_mn + str(val))
        return model_numbers


print(max([int(x) for x in get_valid_model_number(13, 0)]))
# get_valid_model_number(13, 0)
# get_valid_model_number(12, 6)
# get_valid_model_number(11, 174)
