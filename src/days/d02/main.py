import math
import sys

sys.path.append(f'../../..')

def solve(raw_data):
    id_ranges = extract_ranges(raw_data)

    part1 = sum_invalid_ids_in_ranges(id_ranges, max_two_repetitions=True)
    part2 = sum_invalid_ids_in_ranges(id_ranges, max_two_repetitions=False)

    return part1, part2

def sum_invalid_ids_in_ranges(id_ranges, max_two_repetitions):
    sum = 0

    for id_range in id_ranges:
        sum += sum_invalid_ids_in_range(id_range, max_two_repetitions)

    return sum

def sum_invalid_ids_in_range(id_range, max_two_repetitions):
    sum = 0

    for id in range(id_range[0], id_range[1] + 1):
        id_length = math.floor(math.log10(id)) + 1

        repetitions = 1

        while True:
            repetitions += 1

            if repetitions > id_length or (max_two_repetitions and repetitions > 2):
                break

            if id_length % repetitions != 0:
                continue

            sub_length = id_length // repetitions

            sub_values = [(id // (math.pow(10, sub_length * i)) % (math.pow(10, sub_length))) for i in range(repetitions)]

            if (all(sub_value == sub_values[0] for sub_value in sub_values)):
                sum += id
                break

    return sum

def extract_ranges(raw_data):
    id_ranges = [(int(raw_row.split('-')[0]), int(raw_row.split('-')[1])) for raw_row in raw_data.split(',')]

    return id_ranges

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(2).inputfile)))
