import sys

sys.path.append(f'../../..')

def solve(raw_data):
    server_connections = parse_server_connections(raw_data)

    path_count_from_you = count_paths_from_you(server_connections)
    path_count_from_svr = count_paths_from_svr(server_connections)

    return path_count_from_you, path_count_from_svr

def count_paths_from_you(server_connections):
    return recursively_count_paths('you', server_connections, (True, True), {})

def count_paths_from_svr(server_connections):
    return recursively_count_paths('svr', server_connections, (False, False), {})

def recursively_count_paths(server, server_connections, visit_requirements, cache):
    if (server, visit_requirements) in cache:
        return cache[(server, visit_requirements)]

    if server == 'out':
        return 1 if (visit_requirements[0] and visit_requirements[1]) else 0
    
    if server == 'dac':
        visit_requirements = (True, visit_requirements[1])
    
    if server == 'fft':
        visit_requirements = (visit_requirements[0], True)

    result = sum([recursively_count_paths(next_server, server_connections, visit_requirements, cache) for next_server in server_connections[server]])

    cache[(server, visit_requirements)] = result

    return result

def parse_server_connections(raw_data):
    return {raw_row.split(':')[0]: set(raw_row.split(':')[1].split()) for raw_row in raw_data.splitlines()}

if __name__ == '__main__':
    from utility import parse_args_day, print_results, read_data

    print_results(solve(read_data(parse_args_day(11).inputfile)))
