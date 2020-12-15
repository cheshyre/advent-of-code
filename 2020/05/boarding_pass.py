def get_boarding_pass_seat_id(boarding_pass):
    conversion = {
        "F": "0",
        "B": "1",
        "R": "1",
        "L": "0",
    }
    binary = "".join([conversion[x] for x in boarding_pass])
    return int(binary, 2)


def get_boarding_pass_row(boarding_pass):
    conversion = {
        "F": "0",
        "B": "1",
        "R": "1",
        "L": "0",
    }
    binary = "".join([conversion[x] for x in boarding_pass[:-3]])
    return int(binary, 2)


def get_boarding_pass_col(boarding_pass):
    conversion = {
        "F": "0",
        "B": "1",
        "R": "1",
        "L": "0",
    }
    binary = "".join([conversion[x] for x in boarding_pass[-3:]])
    return int(binary, 2)
