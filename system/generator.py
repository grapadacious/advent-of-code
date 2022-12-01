import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

CODE_TEMPLATE = """def part_one(input: list[str]):
    pass

def part_two(input: list[str]):
    pass
"""

CONFIG_TEMPLATE = """{
    "type": "line"
}"""

class Generator:
    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.path = f"{ROOT_DIR}/events/{year}/{day}"
        self.input_path = f"{self.path}/input"

    def generate(self):
        if os.path.exists(self.path):
            print("Directory already exists. Skipping.")
            return

        os.mkdir(self.path)
        os.mkdir(self.input_path)
        self._create_input_file("aoc.txt")
        self._create_input_file("example.txt")
        self._create_code_file()
        self._create_config_file()

    def _create_input_file(self, name):
        with open(f"{self.input_path}/{name}", "w"):
            pass

    def _create_code_file(self):
        with open(f"{self.path}/aoc.py", "w") as file:
            file.write(CODE_TEMPLATE)

    def _create_config_file(self):
        with open(f"{self.path}/config.json", "w") as file:
            file.write(CONFIG_TEMPLATE)
