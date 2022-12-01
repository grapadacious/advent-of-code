import signal
import sys
import re

number_regex = re.compile("\d")
real_number_regex = re.compile("(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def to_number(s):
    if s.isdigit():
        return int(s)

    for i in range(len(number_strings)):
        n = number_strings[i]

        if n == s:
            return i + 1
    
    raise Exception()

def get_number(line, regex):
    numbers = regex.findall(line)

    first = to_number(numbers[0])
    last = to_number(numbers[len(numbers) - 1])

    return (first * 10) + last

def part_one(input):
    total = 0
    for line in input:
        total += get_number(line, number_regex)
    return total

def part_two(input):
    total = 0
    for line in input:
        total += get_number(line, real_number_regex)
    return total

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
