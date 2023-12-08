from read_input import read_input


DAY = 7

CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


def part1() -> int:
    return get_winnings()


def part2() -> int:
    return get_winnings('J')


def get_winnings(joker: str = None) -> int:
    lines = read_input(DAY)
    cards = get_cards(lines)
    cards.sort(key=lambda x: get_card_value(x, joker))
    result = 0
    for i, card in enumerate(cards):
        result += int(card[1]) * (i + 1)

    return result


def get_card_value(card: list[str], joker: str = None) -> int:
    if joker is not None:
        card_values = set_joker(CARD_VALUES, joker)
    else:
        card_values = CARD_VALUES

    hand = card[0]
    value = 0
    value += get_hand_type(hand, joker) * 10**11
    for i, val in enumerate(reversed(hand)):
        value += card_values[val] * 10 ** (2 * i)
    return value


def get_hand_type(hand: str, joker: str) -> int:
    card_dict = get_card_dict(hand)
    joker_count = card_dict.setdefault(joker, 0)
    card_dict[joker] = 0
    key_max = max(card_dict, key=lambda x: card_dict[x])
    card_dict[key_max] += joker_count

    if 5 in card_dict.values():  # Five of a kind
        return 6
    if 4 in card_dict.values():  # Four of a kind
        return 5
    if 3 in card_dict.values() and 2 in card_dict.values():  # Full House
        return 4
    if 3 in card_dict.values():
        return 3
    if 2 in card_dict.values():
        remove_max = list(card_dict.values())
        remove_max.remove(2)
        if 2 in remove_max:
            return 2
        return 1
    return 0


def get_card_dict(hand: str) -> dict[str, int]:
    values = {}
    for sym in hand:
        if sym not in values.keys():
            values[sym] = 1
        else:
            values[sym] += 1
    return values


def get_cards(lines: list[str]) -> list[list[str]]:
    cards = []
    for line in lines:
        cards.append(line.split(' '))
    return cards


def set_joker(card_values: dict[str, int], joker: str) -> dict[str, int]:
    card_values[joker] = 1
    return card_values


if __name__ == "__main__":
    print(part1())
    print(part2())
