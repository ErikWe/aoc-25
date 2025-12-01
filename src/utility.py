def read_data(inputfile):
    return open(inputfile, 'r', encoding='utf-8-sig').read()

def print_results(results):
    print(f'{results[0]} | {results[1]}')