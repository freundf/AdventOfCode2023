from typing import Callable

from read_input import read_input
from math import lcm

DAY = 8


def part1() -> int:
    instructions, _, *lines = read_input(DAY)
    instructions = instructions.strip()
    maps = parse_maps(lines)
    return iterate_maps('AAA', check_end_part1, maps, instructions)


def parse_maps(lines: list[str]) -> dict[tuple[str, str]]:
    maps = {}
    for line in lines:
        name, directions = line.split(" = ")
        left, right = directions.split(", ")
        left = left[1:]
        right = right[:3]
        maps[name] = (left, right)

    return maps


def check_end_part1(current: str) -> bool:
    return current == 'ZZZ'


def iterate_maps(start: str, end_check: Callable[[str], bool], maps: dict[tuple[str, str]], instructions) -> int:
    map_next = start
    count = 0
    while True:
        for direction in instructions:
            if direction == 'L':
                map_next = maps[map_next][0]
            else:
                map_next = maps[map_next][1]

            count += 1
            if end_check(map_next):
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
