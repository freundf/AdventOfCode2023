def read_input(number: int) -> list[str]:
    with open(f"input/{number}") as f:
        return f.readlines()
