import signal
import sys

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

class Subset:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    @property
    def possible(self):
        if self.red > MAX_RED:
            return False
        if self.green > MAX_GREEN:
            return False
        if self.blue > MAX_BLUE:
            return False
        
        return True
    
    @property
    def power(self):
        return self.red * self.green * self.blue

    def load_from(self, string):
        for item in string.split(', '):
            count, color = item.split()

            if color == 'red':
                self.red = int(count)
            elif color == 'green':
                self.green = int(count)
            elif color == 'blue':
                self.blue = int(count)

class Game:
    def __init__(self, line):
        self.id = 0
        self.subsets = []

        self.__parse_input(line)

    @property
    def possible(self):
        result = True

        for subset in self.subsets:
            result = result and subset.possible

        return result
    
    @property
    def power(self):
        return self.minimum_set.power

    @property
    def minimum_set(self):
        result = Subset()

        for subset in self.subsets:
            result.red = max(result.red, subset.red)
            result.green = max(result.green, subset.green)
            result.blue = max(result.blue, subset.blue)
        
        return result
    
    def __parse_input(self, line):
        sections = line.split(': ')
        unparsed_subsets = sections[1].split('; ')
        
        self.id = int(sections[0].split()[1])
        
        self.__parse_subsets(unparsed_subsets)
    
    def __parse_subsets(self, unparsed_subsets):
        for unparsed_subset in unparsed_subsets:
            subset = Subset()
            subset.load_from(unparsed_subset)
            self.subsets.append(subset)


def part_one(input):
    total = 0

    for line in input:
        game = Game(line)
        if game.possible:
            total += game.id
    
    return total

def part_two(input):
    total = 0

    for line in input:
        game = Game(line)
        total += game.power
    
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
