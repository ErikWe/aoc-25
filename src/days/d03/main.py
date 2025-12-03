import sys

sys.path.append(f'../../..')

def solve(raw_data):
    battery_joltages_per_bank = extract_battery_joltages_per_bank(raw_data)

    maximum_total_joltage_two_batteries = find_maximum_total_joltage(battery_joltages_per_bank, 2)
    maximum_total_joltage_twelve_batteries = find_maximum_total_joltage(battery_joltages_per_bank, 12)

    return maximum_total_joltage_two_batteries, maximum_total_joltage_twelve_batteries

def find_maximum_total_joltage(battery_joltages_per_bank, battery_limit):
    joltage = 0

    for battery_joltages in battery_joltages_per_bank:
        joltage += find_maximum_bank_joltage(battery_joltages, battery_limit)

    return joltage

def find_maximum_bank_joltage(battery_joltages, battery_limit):
    joltage = 0
    current_battery_minimum_index = 0
    
    for battery_number in range(battery_limit):
        current_battery_maximum_index = (-(battery_limit - battery_number - 1)) if battery_number != (battery_limit - 1) else None

        battery_range = battery_joltages[current_battery_minimum_index:current_battery_maximum_index]

        battery_index = current_battery_minimum_index + battery_range.index(max(battery_range))

        joltage = joltage * 10 + battery_joltages[battery_index]
        current_battery_minimum_index = battery_index + 1

    return joltage

def extract_battery_joltages_per_bank(raw_data):
    return [[int(battery) for battery in raw_row] for raw_row in raw_data.splitlines()]

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(2).inputfile)))
