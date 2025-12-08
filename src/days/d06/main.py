import numpy as np
import sys

sys.path.append(f'../../..')

def solve(raw_data):
    part1_values, part2_values, operator_delegates = extract_values_and_operators(raw_data)

    part1_sum = sum_operations(part1_values, operator_delegates)
    part2_sum = sum_operations(part2_values, operator_delegates)

    return part1_sum, part2_sum

def sum_operations(values, operator_delegates):
    total_sum = 0

    for i in range(len(operator_delegates)):
        sum = values[i][0]
        
        for j in range(len(values[i]) - 1):
            sum = operator_delegates[i](sum, values[i][j + 1])

        total_sum += sum

    return total_sum

def convert_operators_to_delegates(operators):
    operator_delegates = []

    for operator in operators:
        match operator:
            case '+':
                operator_delegates.append(lambda x, y: x + y)
            case '*':
                operator_delegates.append(lambda x, y: x * y)

    return operator_delegates

def extract_values_and_operators(raw_data):
    operator_delegates = convert_operators_to_delegates(raw_data.splitlines()[-1].split())
    value_matrix = np.array([list(raw_row) for raw_row in raw_data.splitlines()[:-1]])

    part1_values = []
    part2_values = []

    operator_indices = [index for index, potential_operator in enumerate(raw_data.splitlines()[-1]) if potential_operator != ' ']

    for operator_number in range(len(operator_indices)):
        next_operator_index = operator_indices[operator_number + 1] if len(operator_indices) > (operator_number + 1) else (len(value_matrix[0]) + 1)

        new_part1_values = []
        new_part2_values = []

        for row_index in range(len(value_matrix)):
            new_part1_values.append(int(''.join(value_matrix[row_index, operator_indices[operator_number]:next_operator_index])))

        for column_index in range(operator_indices[operator_number], next_operator_index - 1):
            new_part2_values.append(int(''.join(value_matrix[:, column_index])))

        part1_values.append(new_part1_values)
        part2_values.append(new_part2_values)

    return part1_values, part2_values, operator_delegates

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(6).inputfile)))
