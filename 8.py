from typing import Callable
from math import lcm
import re

from read_input import read_input


DAY = 8


def part1() -> int:
    instructions, _, *lines = read_input(DAY)
    instructions = instructions.strip()
    maps = parse_maps(lines)
    return iterate_maps('AAA', check_end_part1, maps, instructions)


def parse_maps(lines: list[str]) -> dict[str, tuple[str, str]]:
    maps = {}
    line_regex = re.compile("(\w{3}) = \((\w{3}), (\w{3})\)")
    for line in lines:
        name, left, right = list(line_regex.search(line).groups())
        maps[name] = (left, right)

    return maps


def check_end_part1(current: str) -> bool:
    return current == 'ZZZ'


def iterate_maps(start: str, end_check: Callable[[str], bool], maps: dict[str, tuple[str, str]], instructions) -> int:
    map_name = start
    count = 0
    while True:
        for direction in instructions:
            map_next = maps[map_name]
            map_name = map_next[0] if direction == 'L' else map_next[1]
            count += 1
            if end_check(map_name):
                return count


def part2() -> int:
    instructions, _, *lines = read_input(8)
    instructions = instructions.strip()
    maps = parse_maps(lines)
    current_maps = [name for name in maps.keys() if name[-1] == 'A']
    counts = []
    for map_cur in current_maps:
        counts.append(iterate_maps(map_cur, check_end_part2, maps, instructions))

    return lcm(*counts)


def check_end_part2(current: str) -> bool:
    return current[-1] == 'Z'


if __name__ == "__main__":
    print(part1())
    print(part2())
