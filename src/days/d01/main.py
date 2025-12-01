import sys

sys.path.append(f'../../..')

def solve(raw_data):
    instructions = extract_instructions(raw_data)

    final_zeros, total_zeros = count_zeros(instructions)

    return final_zeros, total_zeros

def count_zeros(instructions):
    position = 50

    final_zeros = 0
    total_zeros = 0

    for steps in instructions:
        if steps > 100 or steps < -100:
            total_zeros += abs(steps) // 100
            steps = (steps % 100) - (100 if steps < 0 else 0)

        final_position = (position + steps) % 100

        if position != 0 and final_position == 0:
            final_zeros += 1

        if position != 0 and (position + steps > 100 or position + steps < 0 or final_position == 0):
            total_zeros += 1

        position = final_position

    return final_zeros, total_zeros

def extract_instructions(raw_data):
    instructions = [int(raw_row[1:]) * (1 if raw_row[0] == 'R' else -1) for raw_row in raw_data.splitlines()]

    return instructions

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(1).inputfile)))