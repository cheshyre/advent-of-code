"""Module to test interpreter."""

import unittest

import interpreter


class InterpreterPart1Test(unittest.TestCase):
    """Class to test interpreter based on examples in Day 2 Part 1."""

    def test_program1_command1(self):
        """Test the first command of the first program."""
        memory = "1,9,10,3,2,3,11,0,99,30,40,50".split(",")
        memory = [int(x) for x in memory]
        cur_instr = 0

        _ = interpreter.execute_instruction(memory, cur_instr)

        expected_memory = "1,9,10,70,2,3,11,0,99,30,40,50".split(",")
        expected_memory = [int(x) for x in expected_memory]

        self.assertListEqual(memory, expected_memory)

    def test_program1_command1_instr_step(self):
        """Test that first command gives back instruction step 4."""
        memory = "1,9,10,3,2,3,11,0,99,30,40,50".split(",")
        memory = [int(x) for x in memory]
        cur_instr = 0

        instr_step = interpreter.execute_instruction(memory, cur_instr)

        self.assertEqual(instr_step, 4)

    def test_program1_command2(self):
        """Test the second command of the first program."""
        memory = "1,9,10,70,2,3,11,0,99,30,40,50".split(",")
        memory = [int(x) for x in memory]
        cur_instr = 4

        _ = interpreter.execute_instruction(memory, cur_instr)

        expected_memory = "3500,9,10,70,2,3,11,0,99,30,40,50".split(",")
        expected_memory = [int(x) for x in expected_memory]

        self.assertListEqual(memory, expected_memory)

    def test_program1_command2_instr_step(self):
        """Test that second command gives back instruction step 4."""
        memory = "1,9,10,70,2,3,11,0,99,30,40,50".split(",")
        memory = [int(x) for x in memory]
        cur_instr = 4

        instr_step = interpreter.execute_instruction(memory, cur_instr)

        self.assertEqual(instr_step, 4)

    def test_program1_command3(self):
        """Test the third command of the first program."""
        memory = "3500,9,10,70,2,3,11,0,99,30,40,50".split(",")
        memory = [int(x) for x in memory]
        cur_instr = 8

        _ = interpreter.execute_instruction(memory, cur_instr)

        expected_memory = "3500,9,10,70,2,3,11,0,99,30,40,50".split(",")
        expected_memory = [int(x) for x in expected_memory]

        self.assertListEqual(memory, expected_memory)

    def test_program1_command3_instr_step(self):
        """Test that third command gives back instruction step None."""
        memory = "3500,9,10,70,2,3,11,0,99,30,40,50".split(",")
        memory = [int(x) for x in memory]
        cur_instr = 8

        instr_step = interpreter.execute_instruction(memory, cur_instr)

        self.assertEqual(instr_step, None)
