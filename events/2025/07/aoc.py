def beam_splits(input: list[str], start_index: int):
    beam_indexes = set([start_index])

    for i in range(2, len(input), 2):
        line = input[i]

        adds = set()
        removals = set()
        for bi in beam_indexes:
            if line[bi] == "^":
                yield bi
                removals.add(bi)
                adds.add(bi - 1)
                adds.add(bi + 1)

        beam_indexes = beam_indexes - removals
        beam_indexes = beam_indexes.union(adds)

def part_one(input: list[str]):
    return sum(1 for _ in beam_splits(input, input[0].index("S")))

def part_two(input: list[str]):
    start_index = input[0].index("S")
    beams = {start_index: 1}

    for si in beam_splits(input, start_index):
        if si - 1 not in beams:
            beams[si - 1] = 0
        if si + 1 not in beams:
            beams[si + 1] = 0

        beams[si - 1] += beams[si]
        beams[si + 1] += beams[si]

        del beams[si]

    return sum(beams.values())
