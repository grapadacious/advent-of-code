import signal
import sys

def build_card_counts(input):
    result = {}

    for line in input:
        card_number = int(line.split(': ')[0].split()[1])

        result[card_number] = 1

    return result

def get_numbers(line):
    card_number_string, numbers = line.split(': ')

    winning_numbers_string, own_numbers_string = numbers.split(' | ')

    card_number = int(card_number_string.split()[1])
    winning_numbers = set(map(int, winning_numbers_string.split()))
    own_numbers = set(map(int, own_numbers_string.split()))

    return card_number, winning_numbers, own_numbers

def get_count_winning_numbers(line):
    card_number, winning_numbers, own_numbers = get_numbers(line)

    own_winning_numbers = own_numbers.intersection(winning_numbers)

    return card_number, len(own_winning_numbers)

def get_value(line):
    _, count_winning_numbers = get_count_winning_numbers(line)

    if count_winning_numbers == 0:
        return 0

    return 2 ** (count_winning_numbers - 1)

def get_winning_values(input):
    result = []

    for line in input:
        value = get_value(line)

        if value > 0:
            result.append(value)

    return result

def process_duplicates(card_number, count_winning_numbers, card_counts):
    amount_to_add = card_counts[card_number]

    for i in range(card_number + 1, card_number + count_winning_numbers + 1):
        if i not in card_counts:
            break

        card_counts[i] += amount_to_add

    return card_counts

def part_one(input):
    winning_values = get_winning_values(input)

    return sum(winning_values)

def part_two(input):
    card_counts = build_card_counts(input)

    for line in input:
        card_number, count_winning_numbers = get_count_winning_numbers(line)

        card_counts = process_duplicates(card_number, count_winning_numbers, card_counts)

    result = 0

    for k in card_counts:
        result += card_counts[k]
    
    return result

###
#
# System code below
#
###

def use_test():
    args = set(sys.argv[1:])

    return '--test' in args or '-t' in args

def read_input():
    file_name = 'input.txt'

    if use_test():
        print('Using test input...')
        file_name = 'test.txt'

    with open(f'{sys.path[0]}/{file_name}') as file:
        return file.read().splitlines()

def timeout_handler(signum, frame):
    raise TimeoutError()

def run_part(name, function, input):
    signal.signal(signal.SIGALRM, timeout_handler)

    signal.alarm(10)

    try:
        output = function(input)
        print(f'{name}: {output}')
    except TimeoutError:
        print(f'{name}: TIMEOUT')

    signal.alarm(0)

def main():
    input = read_input()

    run_part('Part 1', part_one, input)
    run_part('Part 2', part_two, input)

if __name__ == '__main__':
    main()
