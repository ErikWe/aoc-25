import sys

sys.path.append(f'../../..')

def solve(raw_data):
    return 0, 0

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(10).inputfile)))
