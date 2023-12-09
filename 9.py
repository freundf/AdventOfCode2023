from read_input import read_input
import sys
DAY = 9


def part1() -> int:
    lines = read_input(DAY)
    sequences = [[int(n) for n in line.split(' ')] for line in lines]
    return sum(calc_next_num(sequence) for sequence in sequences)


def part2() -> int:
    lines = read_input(DAY)
    sequences = [[int(n) for n in line.split(' ')[::-1]] for line in lines]
    return sum(calc_next_num(sequence) for sequence in sequences)


def part1_2_oneliner() -> None:
    print(*[(lambda x: sum((f := lambda s: 0 if sum(s) == 0 else s[-1] + f([s[i] - s[i - 1] for i in range(1, len(s))]))(sequence) for sequence in [[int(n) for n in line.split(' ')[::x]] for line in open("input/9")]))(direction) for direction in [1, -1]], sep='\n')


def calc_next_num(sequence: list[int]) -> int:
    if sum(sequence) == 0:
        return 0
    sequence_next = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    return sequence[-1] + calc_next_num(sequence_next)


if __name__ == "__main__":
    print(part1())
    print(part2())
