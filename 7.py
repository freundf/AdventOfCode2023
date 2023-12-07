from read_input import read_input
import re

DAY = 7

CARDS_VALUES = {
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
    lines = read_input(DAY)
    cards = get_cards(lines)
    cards.sort(key=get_card_value)
    result = 0
    for i, card in enumerate(cards):
        result += int(card[1]) * (i + 1)

    return result


def get_card_value(card) -> int:
    hand = card[0]
    value = 0
    value += get_hand_type(hand) * 10**11
    for i, val in enumerate(reversed(hand)):
        value += CARDS_VALUES[val] * 10 ** (2 * i)
    return value


def get_hand_type(hand: str) -> int:
    card_dict = get_card_dict(hand)
    if 5 in card_dict.values():  # Five of a kind
        return 6
    if 4 in card_dict.values():  # Four of a kind
        return 5
    if 3 in card_dict.values() and 2 in card_dict.values():  # Full House
        return 4
    if 3 in card_dict.values():
        return 3
    lst = list(card_dict.values())
    if 2 in card_dict.values():
        lst = list(card_dict.values())
        lst.remove(2)
        if 2 in lst:
            return 2
        return 1
    return 0


def get_card_dict(hand) -> dict[str, int]:
    values = {}
    for sym in hand:
        if not sym in values.keys():
            values[sym] = 1
        else:
            values[sym] += 1
    return values
    
def get_cards(lines):
    cards = []
    for line in lines:
        cards.append(line.split(' '))
    return cards


if __name__ == "__main__":
    print(part1())
