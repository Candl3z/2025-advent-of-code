from pathlib import Path


class Dial:
    def __init__(self, dial_max: int = 99, dial_start: int = 50) -> None:
        self.dial_max = dial_max
        self.total_dial_nums = dial_max + 1
        self.dial_start = dial_start
        self.dial_current = dial_start

    def move_one(self, direction: str) -> int:
        if direction == "R":
            self.dial_current += 1
        elif direction == "L":
            self.dial_current -= 1
        else:
            msg = "Invalid input"
            raise ValueError(msg)

        self.dial_current %= 100

        return self.dial_current

    def move(self, direction: str, distance: int) -> list[int]:
        return [self.move_one(direction) for i in range(distance)]


def day1_part2() -> int:
    with Path("src/advent_of_code_2025/input1.txt").open("r") as f:
        data = f.read()

    split_data = data.split("\n")

    zero_counter = 0
    dial_100 = Dial()

    for i in split_data:
        front = i[:1]
        number_str = i[1:]
        number_int = int(number_str)

        nums_passed = dial_100.move(front, number_int)

        for j in nums_passed:
            if j == 0:
                zero_counter += 1
    return zero_counter
