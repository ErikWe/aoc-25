import sys

sys.path.append(f'../../..')

def solve(raw_data):
    tiles = extract_tiles(raw_data)

    largest_rectangle = find_largest_rectangle(tiles)

    return largest_rectangle, 0

def find_largest_rectangle(tiles):
    largest = 0

    for origin_tile_index, origin_tile in enumerate(tiles):
        for target_tile in tiles[(origin_tile_index + 1):]:
            area = (abs(origin_tile[0] - target_tile[0]) + 1) * (abs(origin_tile[1] - target_tile[1]) + 1)

            if area > largest:
                largest = area

    return largest

def extract_tiles(raw_data):
    return [(int(raw_row.split(',')[0]), int(raw_row.split(',')[1])) for raw_row in raw_data.splitlines()]

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(9).inputfile)))
