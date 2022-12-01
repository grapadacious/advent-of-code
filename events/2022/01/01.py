import sys

input = []

with open(f'{sys.path[0]}/input.txt') as file:
    input = file.read().splitlines()

def main():
    result = 0
    current = 0
    for line in input:
        if line == '':
            result = max(result, current)
            current = 0
            continue
    
        current += int(line)
    
    print(result)

if __name__ == '__main__':
    main()