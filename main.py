import argparse
from datetime import datetime
from system.generator import Generator
from system.runner import Runner

YEAR = datetime.today().strftime('%Y')
DAY = datetime.today().strftime('%d')

parser = argparse.ArgumentParser("aoc", add_help=False)
args = None

FUNCTION_MAP = {
    "init": lambda: Generator(args.year, args.day.zfill(2)).generate(),
    "run": lambda: Runner(args.year, args.day.zfill(2), args.input, int(args.timeout)).run()
}

parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
parser.add_argument("-y", "--year", help="The Advent of Code year to target", default=YEAR)
parser.add_argument("-d", "--day", help="The Advent of Code day to target", default=DAY)
parser.add_argument("-i", "--input", help="The input file to use when running", default="aoc.txt")
parser.add_argument("-t", "--timeout", help="Override the default timeout", default="10", type=int)
parser.add_argument("command", choices=FUNCTION_MAP.keys(), default="run", nargs="?")

args = parser.parse_args()

FUNCTION_MAP[args.command]()
