def convert_decimal_to_36bit_binary(decimal_num):
    a = bin(decimal_num)
    a = a.replace("0b", "")
    missing_len = 36 - len(a)
    a = "0" * missing_len + a
    return a


def mask_decimal_value(decimal_num, mask):
    bin_num = convert_decimal_to_36bit_binary(decimal_num)
    output = ""
    for mask_val, bin_val in zip(mask, bin_num):
        if mask_val != "X":
            output += mask_val
        else:
            output += bin_val
    return int(output, 2)


def mask_decimal_address(dec_addr, mask):
    bin_addr = convert_decimal_to_36bit_binary(dec_addr)
    output = ""
    for mask_val, bin_val in zip(mask, bin_addr):
        if mask_val == "0":
            output += bin_val
        elif mask_val == "1":
            output += "1"
        else:
            output += "X"
    
    floating_addresses = expand_floating_addresses(output)
    return [int(x, 2) for x in floating_addresses]


def expand_floating_addresses(address):
    cur_addresses = [address]
    next_addresses = []
    while "X" in cur_addresses[0]:
        next_addresses += [x.replace("X", "0", 1) for x in cur_addresses]
        next_addresses += [x.replace("X", "1", 1) for x in cur_addresses]
        
        cur_addresses = next_addresses
        next_addresses = []
    
    return cur_addresses


class MaskedMemoryMachine:
    
    def __init__(self):
        
        self.mask = "X" * 36
        self.memory = {}
        
    def set_mask(self, new_mask):
        self.mask = new_mask
        
    def set_memory(self, addr, val):
        self.memory[addr] = mask_decimal_value(val, self.mask)


class MaskedMemoryMachine2:
    
    def __init__(self):
        
        self.mask = "0" * 36
        self.memory = {}
        
    def set_mask(self, new_mask):
        self.mask = new_mask
        
    def set_memory(self, addr, val):
        addresses = mask_decimal_address(addr, self.mask)
        for x in addresses:
            self.memory[x] = val
        