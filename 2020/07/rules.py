class Rule:
    
    def __init__(self, name, children_names, children_counts):
        self.name = name
        self.children_names = children_names
        self.children_counts = children_counts

    @classmethod
    def from_string(cls, some_string):
        name = some_string.strip().split(" bags contain ")[0]
        child_string = some_string.strip().split(" bags contain ")[1]

        children_names = []
        children_counts = []
        if child_string == "no other bags.":
            return cls(name, children_names, children_counts)
    
        children_array = child_string.split(", ")
        for child in children_array:
            child_count = int(child.split()[0])
            child_name = " ".join(child.split()[1:-1])
            
            children_names.append(child_name)
            children_counts.append(child_count)
            
        return cls(name, children_names, children_counts)
    
    def __repr__(self):
        repr_str = f"RULE: {self.name} = "
        
        for name, count in zip(self.children_names, self.children_counts):
            repr_str += f"{name}:{count} "
            
        return repr_str
            