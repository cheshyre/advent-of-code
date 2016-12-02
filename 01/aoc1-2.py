input = 'L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4, L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5, R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5, L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4, L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1, L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2, R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3, L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1, R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2, R4, R3, L5, R4, R2, R1, L5'
input_l = input.split(", ")

state = 0 # 0 is North, 1 is East, 2 is South, 3 is West
x = 0
y = 0
visited = set(["0,0"]) # Set to take advantage of hashing

for i in input_l:
    # Turn
    if i[0] == 'L':
        state -= 1
    else:
        state += 1
    state = state % 4

    # Move 1 point at a time
    w = int(i[1:])
    while w > 0:
        w -= 1
        if state == 0:
            y += 1
        elif state == 1:
            x += 1
        elif state == 2:
            y -= 1
        else:
            x -= 1

        # Check if current location has been visited
        if "{},{}".format(x, y) in visited:
            print("x: {}, y: {}".format(x, y))
            exit(0)
        else:
            visited.add("{},{}".format(x, y))

print("No state was visited twice.")