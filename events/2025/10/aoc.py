class Specification:
    def __init__(self, line):
        segments = line.split(" ")
        self.lights = frozenset([i - 1 for i in range(len(segments[0])) if segments[0][i] == "#"])
        self.buttons = [frozenset([int(n) for n in s[1:len(s) - 1].split(",")]) for s in segments[1:len(segments) - 1]]
        self.joltages = [int(n) for n in segments[-1][1:len(segments[-1]) - 1].split(",")]
        self.matrix = [[1 if i in b else 0 for i in range(len(self.joltages))] for b in self.buttons]

    def fewest_presses_for_lights(self):
        states = set(b for b in self.buttons)

        c = 1
        while self.lights not in states:
            updated_states = set()

            for state in states:
                for b in self.buttons:
                    updated_states.add(state.symmetric_difference(b))

            states = updated_states
            c += 1

        return c

    def __repr__(self):
        r = f"Lights: {set(l for l in self.lights)}\nButtons: {[set(l for l in b) for b in self.buttons]}\nJoltages: {self.joltages}\nMatrix:\n"
        r += "\n".join([f"  {row}" for row in self.matrix])
        return r

def part_one(input: list[str]):
    specifications = [Specification(line) for line in input]

    total = 0
    for spec in specifications:
        total += spec.fewest_presses_for_lights()

    return total

def part_two(input: list[str]):
    specifications = [Specification(line) for line in input]

    total = 0
    for spec in specifications:
        print(spec)
        print()

    return total
