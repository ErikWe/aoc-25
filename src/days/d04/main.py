import sys

sys.path.append(f'../../..')

def solve(raw_data):
    map = extract_map(raw_data)
    neighboring_roll_counts = count_neighboring_rolls(map)

    part1 = count_accessible_rolls(map, neighboring_roll_counts, True)
    part2 = count_accessible_rolls(map, neighboring_roll_counts, False)

    return part1, part2

def count_accessible_rolls(map, neighboring_roll_counts, max_one_iteration):
    map = [row[:] for row in map]
    neighboring_roll_counts = [row[:] for row in neighboring_roll_counts]

    accessible_roll_count = 0

    while True:
        change = False

        for y, row in enumerate(map):
            for x, tile_occupied in enumerate(row):
                if tile_occupied is False:
                    continue

                if neighboring_roll_counts[y][x] < 4:
                    change = True

                    map[y][x] = False
                    accessible_roll_count += 1

                    if max_one_iteration is False:
                        modify_neighboring_tiles(x, y, neighboring_roll_counts, lambda count: count - 1)

        if change is False or max_one_iteration:
            break

    return accessible_roll_count

def count_neighboring_rolls(map):
    neighboring_roll_counts = [[0] * len(row) for row in map]

    for y, row in enumerate(map):
        for x, tile_occupied in enumerate(row):
            if tile_occupied is False:
                continue

            modify_neighboring_tiles(x, y, neighboring_roll_counts, lambda count: count + 1)

    return neighboring_roll_counts

def modify_neighboring_tiles(x, y, map, change_delegate):
    for delta_y in range(-1, 2):
        for delta_x in range(-1, 2):
            if delta_y == 0 and delta_x == 0:
                continue

            if y + delta_y >= 0 and y + delta_y < len(map) and x + delta_x >= 0 and x + delta_x < len(map[0]):
                map[y + delta_y][x + delta_x] = change_delegate(map[y + delta_y][x + delta_x])

def extract_map(raw_data):
    return [[raw_tile == '@' for raw_tile in raw_row] for raw_row in raw_data.splitlines()]

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(4).inputfile)))
