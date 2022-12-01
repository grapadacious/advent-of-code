from . import util

class Run:
    def __init__(self, name, result, output, timeout):
        self.name = name
        self.result = result
        self.output = output
        self.time = 0
        self.timeout = timeout

class Printer:
    def print(self, run: Run):
        print(f"================== {run.name} ==================\n")

        if run.timeout:
            print("Result: TIMEOUT\n")
        else:
            print(f"Result: {run.result}\n")
            print(f"Runtme: {util.ns_to_human(run.time)}\n")
        
        if len(run.output.logs) > 0:
            print("-------------------- LOGS --------------------\n")
            for log in run.output.logs:
                print(log)
            print()

        if len(run.output.errors) > 0:
            print("------------------- ERRORS -------------------\n")
            for error in run.output.errors:
                self._print_error(error)
            print()


    def _print_error(self, error):
        print(f"\033[91m{error}\033[0m")
