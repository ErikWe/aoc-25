import math
import sys

sys.path.append(f'../../..')

def solve(raw_data):
    machines = parse_machines(raw_data)

    minimum_light_button_presses = find_total_minimum_light_button_presses(machines)
    
    return minimum_light_button_presses, 0

def find_total_minimum_light_button_presses(machines):
    return sum([find_minimum_light_button_presses(machine) for machine in machines])

def find_minimum_light_button_presses(machine):
    if sum(machine[0]) == 0:
        return 0
    
    combinations = [combination for combination in range(1, pow(2, len(machine[1])))]

    combinations.sort(key=lambda combination: sum_digits(combination, 2))

    for combination in combinations:
        light_states = [False] * len(machine[0])

        for button_index, button in enumerate(machine[1]):
            if pow(2, button_index) & combination == 0:
                continue

            for light_activation in button:
                light_states[light_activation] ^= True

        if machine[0] == light_states:
            return sum_digits(combination, 2)
        
    return -1

def parse_machines(raw_data):
    return [parse_machine(raw_row) for raw_row in raw_data.splitlines()]

def parse_machine(raw_row):
    lights = [char == '#' for char in raw_row[1:].split(']')[0]]
    buttons = [[int(light) for light in lights[1:-1].split(',')] for lights in raw_row.split(']')[1].split('{')[0].split()]
    joltages = [int(joltage) for joltage in raw_row.split('{')[1][:-1].split(',')]

    return (lights, buttons, joltages)

def sum_digits(value, base):
    count = 0

    for shift in range(math.floor(math.log(value, base)) + 1):
        count += (value // pow(base, shift)) % base

    return count

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(10).inputfile)))
