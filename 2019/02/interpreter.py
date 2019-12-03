"""Module to hold interpreter logic for Intcode."""
from typing import List, Union


def run_program(intcode_ops: List[int]) -> int:
    """Run Intcode program given as list of opcodes."""
    memory = list(intcode_ops)
    cur_instr = 0
    instr_step = 0
    while instr_step is not None:
        print(memory)
        cur_instr += instr_step
        instr_step = execute_instruction(memory, cur_instr)
    return memory[0]


def execute_instruction(memory: List[int], cur_instr: int) -> Union[int, None]:
    """Execute single instruction.

    Returns
    -------
    int or None
        If instruction is an exit, returns `None`;
        otherwise, returns the number of memory addresses to move to reach
        next instruction.

    Notes
    -----
    This operation mutates the state of the memory. Before beginning a
    calculation, it is recommended to make a copy of the Intcode program
    and run on that, as is done in `run_program`.

    """
    cur_opcode = memory[cur_instr]
    if cur_opcode not in SUPPORTED_OPCODES:
        raise ValueError(
            "Opcode {} at {} not supported.".format(cur_opcode, cur_instr)
        )
    return SUPPORTED_OPCODES[cur_opcode](memory, cur_instr)


# -------------------------- Instructions -----------------------------------


def instr_halt(memory: List[int], cur_instr: int) -> Union[int, None]:
    """Execute halt."""
    return None


def instr_add(memory: List[int], cur_instr: int) -> Union[int, None]:
    """Execute add."""
    if cur_instr + 3 >= len(memory):
        raise IndexError(
            "Add at {} made out-of-bounds access".format(cur_instr)
        )
    value = memory[memory[cur_instr + 1]] + memory[memory[cur_instr + 2]]
    memory[memory[cur_instr + 3]] = value
    return 4


def instr_mul(memory: List[int], cur_instr: int) -> Union[int, None]:
    """Execute multiply."""
    if cur_instr + 3 >= len(memory):
        raise IndexError(
            "Mul at {} made out-of-bounds access".format(cur_instr)
        )
    value = memory[memory[cur_instr + 1]] * memory[memory[cur_instr + 2]]
    memory[memory[cur_instr + 3]] = value
    return 4


SUPPORTED_OPCODES = {1: instr_add, 2: instr_mul, 99: instr_halt}
