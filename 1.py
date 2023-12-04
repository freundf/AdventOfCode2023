from read_input import read_input

DAY = 1


def main():
    lines = read_input(DAY)
    digits = {
        "one": 'one1one',
        "two": 'two2two',
        "three": 'three3three',
        "four": 'four4four',
        "five": 'five5five',
        "six": 'six6six',
        "seven": 'seven7seven',
        "eight": 'eight8eight',
        "nine": 'nine9nine'
    }

    result = 0
    for line in lines:
        for key, value in digits.items():
            line = line.replace(key, value)

        numbers = ''.join(c for c in line if c.isdigit())
        result += int(numbers[0] + numbers[-1])

    print(result)


if __name__ == "__main__":
    main()
