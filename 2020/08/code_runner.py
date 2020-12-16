def swap_jmp_and_nop(command):
    if "jmp" in command:
        return command.replace("jmp", "nop")
    return command.replace("nop", "jmp")


class CodeRunner:
    
    def __init__(self, commands):
        self.commands = commands
        self.acc = 0
        self.commands_exec_counts = [0] * len(commands)
        self.instr_ptr = 0
        
    def run_until_repeat(self):
        self.acc = 0
        self.commands_exec_counts = [0] * len(self.commands)
        self.instr_ptr = 0
        
        self.commands_exec_counts[self.instr_ptr] += 1
        while self.commands_exec_counts[self.instr_ptr] < 2:
            # self.print_state()
            command = self.commands[self.instr_ptr]
            operation = command.split()[0]
            argument = int(command.split()[1])
            
            if operation == "nop":
                self.do_nop()
            elif operation == "jmp":
                self.do_jmp(argument)
            elif operation == "acc":
                self.do_acc(argument)
            else:
                print(f"Invalid operation {operation} encountered")
                exit(-1)
                
            # Increment command counts
            if self.instr_ptr < len(self.commands):
                self.commands_exec_counts[self.instr_ptr] += 1
        
    def run_with_flipped_command(self, command_index):
        self.acc = 0
        self.commands_exec_counts = [0] * len(self.commands)
        self.instr_ptr = 0
        
        self.commands[command_index] = swap_jmp_and_nop(self.commands[command_index])
        
        self.commands_exec_counts[self.instr_ptr] += 1
        while self.instr_ptr < len(self.commands) and self.commands_exec_counts[self.instr_ptr] < 2:
            # self.print_state()
            command = self.commands[self.instr_ptr]
            operation = command.split()[0]
            argument = int(command.split()[1])
            
            if operation == "nop":
                self.do_nop()
            elif operation == "jmp":
                self.do_jmp(argument)
            elif operation == "acc":
                self.do_acc(argument)
            else:
                print(f"Invalid operation {operation} encountered")
                exit(-1)
                
            # Increment command counts
            if self.instr_ptr < len(self.commands):
                self.commands_exec_counts[self.instr_ptr] += 1
            
        self.commands[command_index] = swap_jmp_and_nop(self.commands[command_index])
        
        return self.instr_ptr >= len(self.commands)
            
    def do_nop(self):
        self.do_jmp(1)
    
    def do_jmp(self, count):
        self.instr_ptr += count
    
    def do_acc(self, count):
        self.acc += count
        self.do_jmp(1)

    def print_state(self):
        print(f"Acc: {self.acc}")
        print(f"Instr ptr: {self.instr_ptr}")
        print(f"Cur instr: {self.commands[self.instr_ptr]}")
        