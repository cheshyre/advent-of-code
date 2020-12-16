class Bag:
    
    def __init__(self, bag_name):
        self.name = bag_name
        self.children_names = [bag_name]
        self.children_counts = [1]
        self.contained_bags = 0
        
    def is_empty(self):
        return len(self.children_names) == 0
    
    def contains(self, bag_name):
        return bag_name in self.children_names
    
    def unpack_once(self, rules):
        new_children = {}
        
        for name, count in zip(self.children_names, self.children_counts):
            rule = rules[name]
            
            for childname, childcount in zip(rule.children_names, rule.children_counts):
                if childname in new_children:
                    new_children[childname] += count * childcount
                else:
                    new_children[childname] = count * childcount
                    
        new_children_names = []
        new_children_counts = []
        for name in new_children:
            new_children_names.append(name)
            new_children_counts.append(new_children[name])
            
        self.children_counts = new_children_counts
        self.children_names = new_children_names
        self.contained_bags += sum(new_children_counts)
    
    def __repr__(self):
        repr_str = f"BAG: {self.name} = "
        
        for name, count in zip(self.children_names, self.children_counts):
            repr_str += f"{name}:{count} "
            
        return repr_str
        