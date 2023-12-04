from read_input import read_input

DAY: int = 2
CUBE_COUNTS: dict[str, int] = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def part1() -> int:
    lines = read_input(DAY)
    result = 0
    for line in lines:
        title, body = line.split(": ")
        game_id = title.split(" ")[-1]
        if check_game(body):
            result += int(game_id)

    return result


def part2() -> int:
    lines = read_input(DAY)
    result = 0
    for line in lines:
        _, body = line.split(":")
        result += get_power(body)

    return result


def check_game(game: str) -> bool:
    reveals = game.strip().split("; ")
    for reveal in reveals:
        cube_sets = reveal.split(", ")
        for cube_set in cube_sets:
            count, color = cube_set.split(' ')
            if int(count) > CUBE_COUNTS[color]:
                return False

    return True


def get_power(game: str) -> int:
    max_values = {'red': 0, 'green': 0, 'blue': 0}
    reveals = game.strip().split("; ")
    for reveal in reveals:
        cube_sets = reveal.split(", ")
        for cube_set in cube_sets:
            count, color = cube_set.split(' ')
            if int(count) > max_values[color]:
                max_values[color] = int(count)

    power = 1
    for value in max_values.values():
        power *= value

    return power


if __name__ == "__main__":
    print(part1())
    print(part2())
