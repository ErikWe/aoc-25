import sys

sys.path.append(f'../../..')

def solve(raw_data):
    splitter_map, source = extract_splitter_map_and_source(raw_data)

    split_count = count_splits(splitter_map, source, set())
    quantum_split_count = count_quantum_splits(splitter_map, source, {}) + 1

    return split_count, quantum_split_count

def count_splits(splitter_map, source, split_positions):
    count = 0

    position = source

    while True:
        if splitter_map[position[0]][position[1]]:
            if position not in split_positions:
                count += 1
                split_positions.add(position)

                if position[0] + 1 < len(splitter_map):
                    if position[1] > 0:
                        count += count_splits(splitter_map, (position[0] + 1, position[1] - 1), split_positions)
                    if position[1] + 1 < len(splitter_map[0]):
                        count += count_splits(splitter_map, (position[0] + 1, position[1] + 1), split_positions)

            break

        if position[0] + 1 == len(splitter_map):
            break

        position = (position[0] + 1, position[1])

    return count

def count_quantum_splits(splitter_map, source, cache):
    if source in cache:
        return cache[source]
    
    count = 0

    position = source

    while True:
        if splitter_map[position[0]][position[1]]:
            count += 1

            if position[0] + 1 < len(splitter_map):
                if position[1] > 0:
                    count += count_quantum_splits(splitter_map, (position[0] + 1, position[1] - 1), cache)
                if position[1] + 1 < len(splitter_map[0]):
                    count += count_quantum_splits(splitter_map, (position[0] + 1, position[1] + 1), cache)

            break

        if position[0] + 1 == len(splitter_map):
            break

        position = (position[0] + 1, position[1])

    cache[source] = count

    return count

def extract_splitter_map_and_source(raw_data):
    splitter_map = [[tile == '^' for tile in raw_row] for raw_row in raw_data.splitlines()]
    source = (0, raw_data.splitlines()[0].find('S'))

    return splitter_map, source

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(7).inputfile)))
