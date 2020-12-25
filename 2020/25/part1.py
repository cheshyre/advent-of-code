import os

import encryption


# cur_dir = os.path.dirname(os.path.abspath(__file__))

# with open(f"{cur_dir}/input") as f:
#     pass

subject_number = 7
divisor = 20201227

# card_pub_key = 5764801
card_pub_key = 19241437

card_loop_number = 1
card_result = encryption.transform_number_single_iter(1, subject_number, divisor)
print(card_result)
while card_result != card_pub_key:
    card_loop_number += 1
    card_result = encryption.transform_number_single_iter(card_result, subject_number, divisor)
    # print(card_result)
print(card_loop_number)

# door_pub_key = 17807724
door_pub_key = 17346587

door_loop_number = 1
door_result = encryption.transform_number_single_iter(1, subject_number, divisor)
print(door_result)
while door_result != door_pub_key:
    door_loop_number += 1
    door_result = encryption.transform_number_single_iter(door_result, subject_number, divisor)
    # print(door_result)
print(door_loop_number)

print(encryption.transform_number(1, door_pub_key, divisor, card_loop_number))
print(encryption.transform_number(1, card_pub_key, divisor, door_loop_number))
    

