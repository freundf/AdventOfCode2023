from read_input import read_input

DAY = 4


def part1() -> int:
    lines = read_input(DAY)
    result = 0
    for line in lines:
        value_power = -1
        card_num, play_nums, winning_nums = split_card(line)
        for num in play_nums:
            if num in winning_nums:
                value_power += 1

        if value_power > -1:
            result += pow(2, value_power)
    return result


def part2() -> int:
    lines = read_input(DAY)

    for i, line in enumerate(lines):
        win_count = 0
        card_num, play_nums, winning_nums = split_card(line)
        for num in play_nums:
            if num in winning_nums:
                win_count += 1

        for win in range(win_count):
            lines.append(lines[card_num + win])

    return len(lines)


def split_card(card: str) -> (int, list[int], list[int]):
    title, numbers = card.split(": ")
    card_num = int(title.split()[-1])
    play_nums, winning_nums = numbers.split(" | ")
    play_nums = play_nums.split()
    winning_nums = winning_nums.split()
    return card_num, play_nums, winning_nums


if __name__ == "__main__":
    print(part1())
    print(part2())
