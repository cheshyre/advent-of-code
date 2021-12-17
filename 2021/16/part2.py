import os
from typing import Any, Tuple


cur_dir = os.path.dirname(os.path.abspath(__file__))


HEX_TO_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def get_binary_string_from_hex_string(packet_hex: str) -> str:
    return "".join([HEX_TO_BIN[x] for x in packet_hex])


def parse_packet_header(packet_bin: str) -> Tuple[int, int]:
    version = int(packet_bin[0:3], base=2)
    type_id = int(packet_bin[3:6], base=2)

    return version, type_id


def parse_literal_packet_value_and_length(packet_bin: str) -> Tuple[int, int, int, int]:
    version, type_id = parse_packet_header(packet_bin)

    STARTING_OFFSET = 6
    GROUP_SIZE = 5
    start = STARTING_OFFSET
    end = start + GROUP_SIZE

    terminate = False

    value_bin = ""
    while not terminate and end <= len(packet_bin):
        group = packet_bin[start:end]
        value_bin += group[1:]

        if group[0] == "0":
            terminate = True
        else:
            start += GROUP_SIZE
            end += GROUP_SIZE

    if not terminate:
        raise Exception(
            "Packet Type ID 4: Reached end of packet without terminating group"
        )

    print(
        f"PACKET = {packet_bin}\nVERSION = {version}\nTYPE={type_id}\nVALUE = {int(value_bin, base=2)}\n"
    )

    return version, type_id, end, int(value_bin, base=2)


def parse_operator_packet_type0(packet_bin: str) -> Tuple[int, int, int, Any]:
    version, type_id = parse_packet_header(packet_bin)

    LEN_START = 7
    PACKET_START = LEN_START + 15
    start = PACKET_START

    length = int(packet_bin[LEN_START:PACKET_START], base=2) + PACKET_START

    print(
        f"PACKET = {packet_bin}\nVERSION = {version}\nTYPE={type_id}\nSUBPACKETS LENGTH = {length - PACKET_START}\n"
    )

    packet_vals = []
    while start < length:
        subpackets = packet_bin[start:]
        subpacket_val = parse_packet(subpackets)
        subpacket_len = subpacket_val[2]

        packet_vals.append(subpacket_val)

        start += subpacket_len

    return version, type_id, start, packet_vals


def parse_operator_packet_type1(packet_bin: str) -> Tuple[int, int, int, Any]:
    version, type_id = parse_packet_header(packet_bin)

    LEN_START = 7
    PACKET_START = LEN_START + 11
    start = PACKET_START

    num_packets = int(packet_bin[LEN_START:PACKET_START], base=2)

    print(
        f"PACKET = {packet_bin}\nVERSION = {version}\nTYPE={type_id}\nNUM PACKETS = {num_packets}\n"
    )

    packet_vals = []
    for _ in range(num_packets):
        subpackets = packet_bin[start:]
        subpacket_val = parse_packet(subpackets)
        subpacket_len = subpacket_val[2]

        packet_vals.append(subpacket_val)

        start += subpacket_len

    return version, type_id, start, packet_vals


def parse_operator_packet(packet_bin: str) -> Tuple[int, int, int, Any]:

    if packet_bin[6] == "0":
        return parse_operator_packet_type0(packet_bin)

    return parse_operator_packet_type1(packet_bin)


def parse_packet(packet_bin: str) -> Tuple[int, int, int, Any]:
    _, type_id = parse_packet_header(packet_bin)

    if type_id == 4:
        return parse_literal_packet_value_and_length(packet_bin)

    return parse_operator_packet(packet_bin)


def get_packet_version_sum(parsed_packet: Tuple[int, int, int, Any]) -> int:

    version_sum = parsed_packet[0]

    try:
        for x in parsed_packet[3]:
            version_sum += get_packet_version_sum(x)
    except TypeError:
        pass

    return version_sum


def parse_packet_hex(packet_hex: str) -> Tuple[int, int, int, Any]:

    return parse_packet(get_binary_string_from_hex_string(packet_hex))


def evaluate_packet_literal(parsed_packet: Tuple[int, int, int, Any]) -> int:
    return parsed_packet[3]


def evaluate_packet_sum(parsed_packet: Tuple[int, int, int, Any]) -> int:

    return sum([evaluate_packet(x) for x in parsed_packet[3]])


def evaluate_packet_product(parsed_packet: Tuple[int, int, int, Any]) -> int:
    val = 1
    for y in [evaluate_packet(x) for x in parsed_packet[3]]:
        val *= y
    return val


def evaluate_packet_min(parsed_packet: Tuple[int, int, int, Any]) -> int:

    return min([evaluate_packet(x) for x in parsed_packet[3]])


def evaluate_packet_max(parsed_packet: Tuple[int, int, int, Any]) -> int:

    return max([evaluate_packet(x) for x in parsed_packet[3]])


def evaluate_packet_gt(parsed_packet: Tuple[int, int, int, Any]) -> int:

    val1 = evaluate_packet(parsed_packet[3][0])
    val2 = evaluate_packet(parsed_packet[3][1])

    if val1 > val2:
        return 1
    return 0


def evaluate_packet_lt(parsed_packet: Tuple[int, int, int, Any]) -> int:

    val1 = evaluate_packet(parsed_packet[3][0])
    val2 = evaluate_packet(parsed_packet[3][1])

    if val1 < val2:
        return 1
    return 0


def evaluate_packet_eq(parsed_packet: Tuple[int, int, int, Any]) -> int:

    val1 = evaluate_packet(parsed_packet[3][0])
    val2 = evaluate_packet(parsed_packet[3][1])

    if val1 == val2:
        return 1
    return 0


EVALUATOR = {
    0: evaluate_packet_sum,
    1: evaluate_packet_product,
    2: evaluate_packet_min,
    3: evaluate_packet_max,
    4: evaluate_packet_literal,
    5: evaluate_packet_gt,
    6: evaluate_packet_lt,
    7: evaluate_packet_eq,
}


def evaluate_packet(parsed_packet: Tuple[int, int, int, Any]) -> int:
    return EVALUATOR[parsed_packet[1]](parsed_packet)


with open(f"{cur_dir}/input") as f:
    packet_hex = f.readline().strip()

print(evaluate_packet(parse_packet_hex(packet_hex)))