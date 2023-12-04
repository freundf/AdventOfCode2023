from read_input import read_input
from functools import cache

DAY = 4


def part1() -> int:
    lines = read_input(DAY)
    result = 0
    for line in lines:
        card_num, (play_nums, winning_nums) = split_card(line)
        hits = set(play_nums).intersection(set(winning_nums))
        if len(hits) > 0:
            result += pow(2, len(hits) - 1)
    return result


def part2() -> int:
    lines = read_input(DAY)
    result = 0
    cards = tuple(split_card(line) for line in lines)
    for i, _ in enumerate(cards):
        result += check_win(i, cards)
    return result


@cache
def check_win(number, cards):
    win_count = 0
    result = 1
    if number + 1 >= len(cards):
        return result

    play_nums, winning_nums = cards[number][1]
    for num in play_nums:
        if num in winning_nums:
            win_count += 1

    for i in range(win_count):
        result += check_win(number + i + 1, cards)

    return result


def split_card(card: str) -> (int, (int, int)):
    title, numbers = card.split(": ")
    card_num = int(title.split()[-1])
    play_nums, winning_nums = numbers.split(" | ")
    play_nums = tuple(play_nums.split())
    winning_nums = tuple(winning_nums.split())
    return card_num, (play_nums, winning_nums)


if __name__ == "__main__":
    print(part1())
    print(part2())
