class RuleType1:
    
    def __init__(self, min_num: int, max_num: int, character: str):
        self.min_num = min_num
        self.max_num = max_num 
        self.character = character 
        
    @classmethod
    def from_string(cls, str_to_parse: str):
        min_val = int(str_to_parse.split()[0].split("-")[0])
        max_val = int(str_to_parse.split()[0].split("-")[1])
        character = str_to_parse.split()[1]
        
        return cls(min_val, max_val, character)

    def check_string(self, input_string: str) -> bool:
        counts = input_string.count(self.character)
        if counts < self.min_num:
            return False
        if counts > self.max_num:
            return False
        return True
    
    
class RuleType2:
    
    def __init__(self, index_1: int, index_2: int, character: str):
        self.index_1 = index_1
        self.index_2 = index_2 
        self.character = character 
        
    @classmethod
    def from_string(cls, str_to_parse: str):
        index_1 = int(str_to_parse.split()[0].split("-")[0])
        index_2 = int(str_to_parse.split()[0].split("-")[1])
        character = str_to_parse.split()[1]
        
        return cls(index_1, index_2, character)

    def check_string(self, input_string: str) -> bool:
        return (input_string[self.index_1 - 1] == self.character) != (input_string[self.index_2 - 1] == self.character)
