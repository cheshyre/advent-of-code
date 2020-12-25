def transform_number(input_num, subject_number, divisor, loop_number):
    # if loop_number == 1:
    #     prev_number = input_num
    # else:
    #     prev_number = transform_number(input_num, subject_number, divisor, loop_number - 1)
    prev_number = input_num
    for _ in range(loop_number):
        prev_number = (prev_number * subject_number) % divisor
    return prev_number


def transform_number_single_iter(input_num, subject_number, divisor):
    return (input_num * subject_number) % divisor
