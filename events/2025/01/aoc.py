def part_one(input):
    pos = 50
    count = 0

    for line in input:
        if line[0] == "R":
            pos += int(line[1:])
        else:
            pos -= int(line[1:])

        pos = pos % 100

        if pos == 0:
            count += 1

    return count

def part_two(input):
    pos = 50
    count = 0

    for line in input:
        direction = line[0]
        rotation = int(line[1:])

        if rotation > 100:
            count += rotation // 100
            rotation = rotation % 100

        if direction == "R":
            pos += rotation

            if pos > 100:
                count += 1
        else:
            prev = pos
            pos -= rotation

            if pos < 0 and prev != 0:
                count += 1

        pos = pos % 100

        if pos == 0:
            count += 1

    return count
