from read_input import read_input
from collections import namedtuple

DAY = 3

Number = namedtuple('number', ['start', 'end'])


def part1() -> int:
    result = 0
    lines = read_input(DAY)
    line_numbers = []
    for line in lines:
        line_numbers.append(find_numbers(line))

    for i, line in enumerate(line_numbers):
        for number in line:
            if check_surroundings(lines, i, number.start, number.end):
                result += get_value(lines, i, number)

    return result


def get_value(lines: list[str], line_index: int, number: Number) -> int:
    value = ""
    for i in range(number.start, number.end + 1):
        value += lines[line_index][i]
    return int(value)


def find_numbers(line: str) -> list[Number]:
    numbers: list[Number] = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            start = i
            while line[i + 1].isdigit():
                i += 1
            end = i
            numbers.append(Number(start, end))
        i += 1
    return numbers


def check_surroundings(lines: list[str], line_index: int, start: int, end: int) -> bool:
    for i in range(start - 1, end + 2):
        if 0 <= i < len(lines[line_index]):
            if line_index != 0 and is_special(lines[line_index - 1][i]):
                return True
            if line_index != len(lines) - 1 and is_special(lines[line_index + 1][i]):
                return True
            if is_special(lines[line_index][i]):
                return True
    return False


def is_special(char: str) -> bool:
    return not (char.isdigit() or char == '.' or char == '\n')


def part2() -> int:
    result = 0
    lines = read_input(DAY)
    line_numbers = []
    gears = {}
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            gears[(i, j)] = []

    for line in lines:
        line_numbers.append(find_numbers(line))

    for i, line in enumerate(line_numbers):
        gears: dict[tuple[int, int], list[int, int]]
        for number in line:
            check_gears(gears, lines, i, number)

    for gear in gears.values():
        if len(gear) == 2:
            result += gear[0] * gear[1]

    return result


def check_gears(gears, lines: list[str], line_index: int, number: Number) -> None:
    for i in range(number.start - 1, number.end + 2):
        if 0 <= i < len(lines[line_index]):
            if line_index != 0 and lines[line_index - 1][i] == '*':
                gears[(i, line_index - 1)].append(get_value(lines, line_index, number))
            if line_index != len(lines) - 1 and lines[line_index + 1][i] == '*':
                gears[(i, line_index + 1)].append(get_value(lines, line_index, number))
            if lines[line_index][i] == '*':
                gears[(i, line_index)].append(get_value(lines, line_index, number))


if __name__ == "__main__":
    print(part1())
    print(part2())
