from read_input import read_input

DAY = 11


def part1() -> int:
    lines = [[char for char in line.strip()] for line in read_input(DAY)]
    galaxies = find_galaxies(lines)
    distances = [[1 for _ in line] for line in lines]
    fact_exp = 2
    distances = expand(distances, galaxies, fact_exp)
    return get_distance_sum(distances, galaxies)


def part2() -> int:
    lines = [[char for char in line.strip()] for line in read_input(DAY)]
    galaxies = find_galaxies(lines)
    distances = [[1 for _ in line] for line in lines]
    fact_exp = 1000000
    distances = expand(distances, galaxies, fact_exp)
    return get_distance_sum(distances, galaxies)


def get_distance_sum(distances: list[list[int]], galaxies: list[list[int, int]]) -> int:
    result = 0
    galaxy_set = set(tuple((a, b) for a, b in galaxies))
    while len(galaxy_set) != 0:
        next_galaxy = galaxy_set.pop()
        for galaxy in galaxy_set:
            distance = 0
            next = [next_galaxy[0], next_galaxy[1]]
            while next[0] != galaxy[0]:
                next[0] += 1 if next[0] < galaxy[0] else -1
                distance += distances[next[0]][next[1]]
            while next[1] != galaxy[1]:
                next[1] += 1 if next[1] < galaxy[1] else -1
                distance += distances[next[0]][next[1]]
            result += distance

    return result


def find_galaxies(lines: list[list[str]]) -> list[list[int, int]]:
    galaxies = []
    for i, line in enumerate(lines):
        for j, sym in enumerate(line):
            if sym == '#':
                galaxies.append([i, j])
    return galaxies


def expand(lines: list[list[int]], galaxies: list[list[int, int]], factor_expand: int) -> list[list[int]]:
    x_galaxies = [galaxy[0] for galaxy in galaxies]
    empty_lines = []
    for n in range(len(lines)):
        if n not in x_galaxies:
            empty_lines.append(n)

    y_galaxies = [galaxy[1] for galaxy in galaxies]
    empty_columns = []
    for n in range(len(lines[0])):
        if n not in y_galaxies:
            empty_columns.append(n)

    for i in empty_lines:
        for j in range(len(lines[0])):
            lines[i][j] = factor_expand

    for i in range(len(lines)):
        for j in empty_columns:
            lines[i][j] = factor_expand

    return lines


if __name__ == "__main__":
    print(part1())
    print(part2())
