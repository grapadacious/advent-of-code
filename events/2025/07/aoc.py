def part_one(input: list[str]):
    beam_indexes = set([input[0].index("S")])

    total = 0
    for i in range(1, len(input)):
        line = input[i]

        adds = set()
        removals = set()
        for bi in beam_indexes:
            if line[bi] == "^":
                total += 1
                removals.add(bi)
                adds.add(bi - 1)
                adds.add(bi + 1)

        beam_indexes = beam_indexes - removals
        beam_indexes = beam_indexes.union(adds)

    return total

def remove(original: list[int], removals: set[int]):
    result = []
    for n in original:
        if n not in removals:
            result.append(n)

    return result

def part_two(input: list[str]):
    beams = {input[0].index("S"): 1}

    for i in range(2, len(input), 2):
        line = input[i]

        removals = set()
        keys = [k for k in beams.keys()]

        for bi in keys:
            if line[bi] == "^":
                if (bi - 1) not in beams:
                    beams[bi - 1] = beams[bi]
                else:
                    beams[bi - 1] += beams[bi]
                
                if bi + 1 not in beams:
                    beams[bi + 1] = beams[bi]
                else:
                    beams[bi + 1] += beams[bi]

                removals.add(bi)

        for r in removals:
            del beams[r]

    return sum(beams.values())

