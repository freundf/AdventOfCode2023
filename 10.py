from read_input import read_input
from collections import namedtuple

DAY = 10

point = namedtuple('point', ['x', 'y'])
class Point:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

DIRECTIONS = {
    '-': (point(-1, 0), point(1, 0)),
    '|': (point(0, -1), point(0, 1)),
    'L': (point(0, -1), point(1, 0)),
    'J': (point(0, -1), point(-1, 0)),
    '7': (point(0, 1), point(-1, 0)),
    'F': (point(0, 1), point(1, 0)),
    'S': (point(0, 1), point(0, -1), point(1, 0), point(-1, 0)),
    '.': ()
}


def part1() -> int:
    grid = [line.strip() for line in read_input(DAY)]
    start = find_start(grid)
    return len(find_loop(grid, start)) // 2


def part2() -> int:
    grid = [line.strip() for line in read_input(DAY)]
    start = find_start(grid)
    loop = find_loop(grid, start)
    result = 0
    for y, line in enumerate(grid):
        count = 0
        bool1 = bool2 = False
        for x, sym in enumerate(line):
            pos = point(x, y)
            if pos in loop and sym in ['|', 'L', 'J']:
                bool1 = not bool1
            if pos in loop and sym in ['|', '7', 'F']:
                bool2 = not bool2
            if bool1 and bool2 and pos not in loop:
                count += 1
        result += count
    return result


def find_loop(grid, start):
    found = {start}
    nodes = {neighbour for neighbour in find_neighbours(grid, start) if start in find_neighbours(grid, neighbour)}
    while len(nodes) != 0:
        next_node = nodes.pop()
        found.add(next_node)
        nodes = nodes.union(find_neighbours(grid, next_node).difference(found))
    return found


def find_neighbours(grid: list[str], pos: point) -> set[point]:
    return {point(pos.x + direction.x, pos.y + direction.y) for direction in DIRECTIONS[grid[pos.y][pos.x]]}


def find_start(grid: list[str]) -> point:
    for y, line in enumerate(grid):
        for x, sym in enumerate(line):
            if sym == 'S':
                return point(x, y)
    assert False


if __name__ == "__main__":
    print(part1())
    print(part2())
