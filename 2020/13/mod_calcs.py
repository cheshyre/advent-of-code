def find_new_start(start, jump, divisor, offset):
    for i in range(start, jump * divisor + 1, jump):
        if (i + offset) % divisor == 0:
            return i
    return -1


def get_timestamp(main_bus, next_buses, offsets):
    start = 0
    jump = main_bus
    for bus, offset in zip(next_buses, offsets):
        start = find_new_start(start, jump, bus, offset)
        jump *= bus
    return start
