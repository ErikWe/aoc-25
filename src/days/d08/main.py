import math
import sys

sys.path.append(f'../../..')

def solve(raw_data):
    connection_count = 1000

    boxes = extract_boxes(raw_data)
    networks = [[box] for box in boxes]

    squared_box_distances = compute_squared_box_distances(boxes)

    networks = connect_networks_limit(networks, squared_box_distances, connection_count)

    part1 = multiply_largest_networks(networks)
    part2 = get_last_connection_product(networks, squared_box_distances[(connection_count + 1):])

    return part1, part2

def multiply_largest_networks(networks):
    return math.prod(sorted([len(network) for network in networks], reverse=True)[:3])

def connect_networks_limit(networks, squared_box_distances, connection_count):
    network_association = {network[0]:i for i, network in enumerate(networks)}

    for i in range(connection_count):
        left_box_network_index = network_association[squared_box_distances[i][0]]
        right_box_network_index = network_association[squared_box_distances[i][1]]

        if left_box_network_index == right_box_network_index:
            continue

        for box in networks[right_box_network_index]:
            network_association[box] = left_box_network_index

        networks[left_box_network_index].extend(networks[right_box_network_index])
        networks[right_box_network_index] = []

    return networks

def get_last_connection_product(networks, squared_box_distances):
    active_networks = len([network for network in networks if len(network) > 0])
    network_association = {box: network_index for network_index, network in enumerate(networks) for box in network}

    for i in range(len(squared_box_distances)):
        left_box_network_index = network_association[squared_box_distances[i][0]]
        right_box_network_index = network_association[squared_box_distances[i][1]]

        if left_box_network_index == right_box_network_index:
            continue

        if active_networks == 2:
            return squared_box_distances[i][0][0] * squared_box_distances[i][1][0]

        for box in networks[right_box_network_index]:
            network_association[box] = left_box_network_index

        networks[left_box_network_index].extend(networks[right_box_network_index])
        networks[right_box_network_index] = []
        active_networks -= 1

def compute_squared_box_distances(boxes):
    squared_box_distances = []

    for left_box_index, left_box in enumerate(boxes):
        for right_box in boxes[(left_box_index + 1):]:
            squared_distance = pow(left_box[0] - right_box[0], 2) + pow(left_box[1] - right_box[1], 2) + pow(left_box[2] - right_box[2], 2)

            squared_box_distances.append((left_box, right_box, squared_distance))

    return sorted(squared_box_distances, key=lambda x: x[2])

def extract_boxes(raw_data):
    return [(int(raw_row.split(',')[0]), int(raw_row.split(',')[1]), int(raw_row.split(',')[2])) for raw_row in raw_data.splitlines()]

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(8).inputfile)))
