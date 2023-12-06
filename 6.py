from read_input import read_input
from collections import namedtuple
import re
from math import ceil, floor, sqrt

DAY = 6

boat_race = namedtuple("boat_race", ["time", "record"])


def part1() -> int:
    lines = read_input(DAY)
    races = get_races(lines)
    result = 1
    for race in races:
        result *= calc_race_solutions(race)
    return result


def calc_race_solutions(race: boat_race) -> int:
    # final_distance = x * (time - x), using reduced quadratic formula:
    epsilon = 10 ** -6  # used to ensure we actually beat the record
    root = sqrt((race.time * race.time) / 4 - (race.record + epsilon))
    lower = race.time / 2 - root
    upper = race.time / 2 + root
    return floor(upper) - ceil(lower) + 1


def get_races(lines: [str]) -> [boat_race]:
    races = []
    times = split_line(lines[0])
    distances = split_line(lines[1])
    for pair in zip(times, distances):
        races.append(boat_race(pair[0], pair[1]))
    return races


def split_line(line: str) -> [int]:
    result = line.split(":")[1].strip()
    result = re.split(" +", result)
    return [int(_) for _ in result]


def part2() -> int:
    lines = read_input(DAY)
    race = get_race(lines)
    return calc_race_solutions(race)


def get_race(lines: [str]) -> [boat_race]:
    time = split_ignore_whitespace(lines[0])
    distance = split_ignore_whitespace(lines[1])
    return boat_race(time, distance)


def split_ignore_whitespace(line: str) -> [int]:
    values = line.split(":")[1].strip()
    result = ""
    for char in values:
        result += char if char.isdigit() else ""
    return int(result)


if __name__ == "__main__":
    print(part1())
    print(part2())
