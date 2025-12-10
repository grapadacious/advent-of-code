import importlib
import json
import os
import signal
import sys
import time
import traceback
from . import util
from .console import ConsoleOutput
from .printer import Printer, Run
from .readers import ReaderFactory

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def timeout_handler(signum, frame):
    raise TimeoutError()

class Runner:
    def __init__(self, year, day, input_file, timeout=10):
        self.path = f"{ROOT_DIR}/events/{year}/{day}"
        self.input_file = input_file
        self.aoc = importlib.import_module(f"events.{year}.{day}.aoc")
        self.input = self._read_input()
        self.printer = Printer()
        self.runs = []
        self.timeout = timeout

    def run(self):
        self._run_part(self.aoc.part_one)
        self._run_part(self.aoc.part_two)

        self._print_results()

    def _read_input(self):
        type = "line"

        with open(f"{self.path}/config.json") as file:
            config = json.load(file)
            type = config["type"]

        with open(f'{self.path}/input/{self.input_file}') as file:
            return ReaderFactory.create(type, file).read()
        
    def _run_part(self, function):
        run = Run(util.snake_to_caps(function.__name__), None, ConsoleOutput(), False)

        with run.output:
            signal.signal(signal.SIGALRM, timeout_handler)

            signal.alarm(self.timeout)

            try:
                start = time.perf_counter_ns()
                run.result = function(self.input)
                end = time.perf_counter_ns()

                run.time = end - start
            except TimeoutError:
                run.timeout = True
            except:
                sys.stderr.write(traceback.format_exc())

            signal.alarm(0)

        self.runs.append(run)

    def _print_results(self):
        for run in self.runs:
            self.printer.print(run)
