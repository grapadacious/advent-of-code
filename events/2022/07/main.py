import sys

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

def process_line(line):
    segments = line.split(' ')

    if segments[0] == '$' or segments[0] == 'dir':
        return segments

    segments[0] = int(segments[0])

    return segments

def is_command(segments):
    return segments[0] == '$'

def is_ls(segments):
    return is_command(segments) and segments[1] == 'ls'

def is_cd(segments):
    return is_command(segments) and segments[1] == 'cd'

def is_cd_parent(segments):
    return is_cd(segments) and segments[2] == '..'

def is_dir(segments):
    return segments[0] == 'dir'

def goto_location(filesystem, path):
    location = filesystem

    for segment in path:
        location = location[segment][1]

    return location

def build_filesystem(input):
    filesystem = {'/': ['dir', {}]}
    location = filesystem
    path = []

    for line in input:
        segments = process_line(line)

        if is_ls(segments):
            continue
            
        if is_cd_parent(segments):
            path.pop()
            location = goto_location(filesystem, path)
            continue

        if is_cd(segments):
            path.append(segments[2])
            location = location[segments[2]][1]
            continue

        if is_dir(segments):
            if segments[1] not in location:
                location[segments[1]] = ['dir', {}]
            continue

        location[segments[1]] = ['file', segments[0]]

    return filesystem

def total_below(sizes, threshold):
    total = 0

    for size in sizes:
        if size <= threshold:
            total += size
    
    return total

def smallest_above(sizes, threshold, max_value):
    smallest = max_value

    for size in sizes:
        if size >= threshold and size < smallest:
            smallest = size

    return smallest

def find_size(directory):
    size = 0
    all = []

    for key in directory.keys():
        value = directory[key]

        if value[0] == 'file':
            size += value[1]
            continue
            
        s, a = find_size(value[1])

        all.extend(a)

        size += s

    all.append(size)

    return size, all


def part_one(input):
    filesystem = build_filesystem(input)

    threshold = 100_000

    size, all_sizes = find_size(filesystem)

    total = total_below(all_sizes, threshold)
    
    return total

def part_two(input):
    filesystem = build_filesystem(input)

    max_size = 70_000_000
    needed = 30_000_000

    size, all_sizes = find_size(filesystem)

    needed = needed - (max_size - size)

    smallest = smallest_above(all_sizes, needed, max_size)

    return smallest

def main():
    input = read_input()

    part_one_output = part_one(input)
    part_two_output = part_two(input)

    print(f'Part 1: {part_one_output}')
    print(f'Part 2: {part_two_output}')


if __name__ == '__main__':
    main()
