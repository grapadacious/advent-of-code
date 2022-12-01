import sys

input = []

with open(f'{sys.path[0]}/input.txt') as file:
    input = file.read().splitlines()

def find_totals():
    totals = []
    current = 0

    for line in input:
        if line == '':
            totals.append(current)
            current = 0
            continue
    
        current += int(line)

    return totals

def main():
    totals = find_totals()
    
    totals.sort(reverse=True)

    print(sum(totals[:3]))

if __name__ == '__main__':
    main()