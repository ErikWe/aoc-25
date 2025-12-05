import argparse

def read_data(inputfile):
    return open(inputfile, 'r', encoding='utf-8-sig').read()

def print_results(results):
    print(f'{results[0]} | {results[1]}')

def parse_args_day(day):
    parser = argparse.ArgumentParser(description=f'Advent of Code 2024 - Day {day:02d}')
    parser.add_argument('inputfile', help='The file containing the input data')

    return parser.parse_args()
