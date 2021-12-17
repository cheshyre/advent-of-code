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


with open(f"{cur_dir}/input") as f:
    packet_hex = f.readline().strip()

# print(parse_packet("110100101111111000101000"))
# print(parse_packet("00111000000000000110111101000101001010010001001000000000"))
# print(parse_packet("11101110000000001101010000001100100000100011000001100000"))

# print(get_packet_version_sum(parse_packet_hex("8A004A801A8002F478")))
# print(get_packet_version_sum(parse_packet_hex("A0016C880162017C3686B18A3D4780")))
print(get_packet_version_sum(parse_packet_hex(packet_hex)))