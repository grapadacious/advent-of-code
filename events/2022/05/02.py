import sys

steps = []

crates = {}

def process_crates(crate_diagram):
    result = {}
    name_row = crate_diagram[len(crate_diagram) - 1]

    for i in range(1, len(name_row), 4):
        key = int(name_row[i])
        result[key] = []

        for j in range(len(crate_diagram) - 2, -1, -1):
            if crate_diagram[j][i] == ' ':
                continue

            result[key].append(crate_diagram[j][i])

    return result



def process_steps(step_strings):
    result = []

    for line in step_strings:
        split = line.split(' ')

        line_step = []
        for i in range(1, len(split), 2):
            line_step.append(int(split[i]))

        result.append(line_step)

    return result 


with open(f'{sys.path[0]}/input.txt') as file:
    split_input = file.read().split('\n\n')
    
    crates = process_crates(split_input[0].splitlines())
    steps = process_steps(split_input[1].splitlines())

def perform_steps():
    for step in steps:
        step_stack = []
        for n in range(step[0]):
            step_stack.append(crates[step[1]].pop())
            
        while len(step_stack) > 0:
            crates[step[2]].append(step_stack.pop())

def print_result():
    result = ''

    for k in crates.keys():
        result += crates[k].pop()

    print(result)

def main():    
    perform_steps()
    print_result()


if __name__ == '__main__':
    main()
