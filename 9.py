from read_input import read_input

DAY = 9


def part1() -> int:
    lines = read_input(DAY)
    sequences = [[int(n) for n in line.split(' ')] for line in lines]
    return sum(calc_next_num(sequence) for sequence in sequences)


def part2() -> int:
    lines = read_input(DAY)
    sequences = [[int(n) for n in line.split(' ')[::-1]] for line in lines]
    return sum(calc_next_num(sequence) for sequence in sequences)


def calc_next_num(sequence: list[int]) -> int:
    if sum(sequence) == 0:
        return 0
    sequence_next = [sequence[i] - sequence[i - 1] for i in range(1,len(sequence))]
    return sequence[-1] + calc_next_num(sequence_next)


if __name__ == "__main__":
    # print(part1())
    print(part2())
