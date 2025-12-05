import os
import sys

sys.path.append(f'../../..')

def solve(raw_data):
    fresh_ranges, ingredients = extract_fresh_ranges_and_ingredients(raw_data)

    fresh_ranges = iteratively_combine_fresh_ranges(fresh_ranges)

    fresh_ingredients_count = count_fresh_ingredients(fresh_ranges, ingredients)
    total_range_entries = count_total_range_entries(fresh_ranges)

    return fresh_ingredients_count, total_range_entries

def count_total_range_entries(fresh_ranges):
    count = 0

    for fresh_range in fresh_ranges:
        count += fresh_range[1] - fresh_range[0] + 1

    return count    

def count_fresh_ingredients(fresh_ranges, ingredients):
    fresh_ingredients_count = 0

    for ingredient in ingredients:
        found_match = False

        for fresh_range in fresh_ranges:
            if ingredient >= fresh_range[0] and ingredient <= fresh_range[1]:
                fresh_ingredients_count += 1
                found_match = True
                break

        if found_match:
            continue

    return fresh_ingredients_count

def iteratively_combine_fresh_ranges(fresh_ranges):
    while True:
        initial_count = len(fresh_ranges)

        fresh_ranges = combine_fresh_ranges(fresh_ranges)

        if len(fresh_ranges) == initial_count:
            break

    return fresh_ranges

def combine_fresh_ranges(fresh_ranges):
    combined_fresh_ranges = []

    for fresh_range in fresh_ranges:
        combined = False

        for i, combined_fresh_range in enumerate(combined_fresh_ranges):
            if fresh_range[0] >= combined_fresh_range[0] and fresh_range[1] <= combined_fresh_range[1]:
                combined = True
                break

            if fresh_range[0] <= combined_fresh_range[0] and fresh_range[1] >= combined_fresh_range[1]:
                combined_fresh_ranges[i] = fresh_range
                combined = True
                break

            if fresh_range[0] >= combined_fresh_range[0] and fresh_range[0] <= combined_fresh_range[1]:
                combined_fresh_ranges[i] = (combined_fresh_range[0], fresh_range[1])
                combined = True
                break

            if fresh_range[1] >= combined_fresh_range[0] and fresh_range[1] <= combined_fresh_range[1]:
                combined_fresh_ranges[i] = (fresh_range[0], combined_fresh_range[1])
                combined = True
                break

        if combined is False:
            combined_fresh_ranges.append(fresh_range)

    return combined_fresh_ranges


def extract_fresh_ranges_and_ingredients(raw_data):
    sections = raw_data.split(os.linesep + os.linesep)

    fresh_ranges = [(int(raw_row.split('-')[0]), int(raw_row.split('-')[1])) for raw_row in sections[0].splitlines()]
    ingredients = [int(raw_row) for raw_row in sections[1].splitlines()]

    return fresh_ranges, ingredients

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(5).inputfile)))
