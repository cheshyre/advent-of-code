def do_cup_rotation(cups, min_val, max_val):
    cur_cup = cups[0]
    moved_cups = cups[1:4]
    dest_cup = cur_cup - 1
    if dest_cup < min_val:
        dest_cup = max_val
    while dest_cup in moved_cups:
        dest_cup -= 1
        if dest_cup < min_val:
            dest_cup = max_val
    
    dest_index = cups.index(dest_cup)
    # print(dest_index)
    new_cups = cups[4:dest_index + 1] + moved_cups + cups[dest_index + 1:] + [cur_cup]
    return new_cups


def do_cup_rotation_new(cups_dict, cur_id, min_val, max_val):
    moved_ids = []
    cur_cup_saved = cups_dict[cur_id]
    cur_cup = cups_dict[cur_id]
    for _ in range(3):
        cur_cup = cur_cup.next
        moved_ids.append(cur_cup.name)
    
    # Remove cups from ring
    cur_cup_saved.next = cur_cup.next
    dest_id = cur_id - 1
    if dest_id < min_val:
        dest_id = max_val
    while dest_id in moved_ids:
        dest_id -= 1
        if dest_id < min_val:
            dest_id = max_val
    insert_cup_before = cups_dict[dest_id]
    insert_cup_after = insert_cup_before.next
    
    # Insert cups back into ring
    insert_cup_before.next = cups_dict[moved_ids[0]]
    cups_dict[moved_ids[-1]].next = insert_cup_after
    
    return cur_cup_saved.next.name
    

class Cup:
    
    def __init__(self, name):
        self.name = name
        self.next = None

    def __repr__(self):
        return str(self.name)
