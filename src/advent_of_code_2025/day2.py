import re
from pathlib import Path


def check_invalid(num: int, *, exactly_twice: bool) -> bool:
    input_str = str(num)

    search_str = r"\b(\d+)\1\b" if exactly_twice else r"\b(\d+)\1+\b"

    match = re.search(search_str, input_str)

    return match is not None


def get_invalid(start: int, end: int, *, exactly_twice: bool = True) -> list[int]:
    return [num for num in range(start, end + 1) if check_invalid(num, exactly_twice=exactly_twice)]


def get_input() -> list[tuple]:
    with Path("src/advent_of_code_2025/input2.txt").open("r") as f:
        data = f.read().strip()

    split_data = data.split(",")
    return [tuple(map(int, i.split("-"))) for i in split_data]


def day2_part1() -> int:
    start_end_tuple_list = get_input()

    all_invalid_ids_list = [
        i
        for start, end in start_end_tuple_list
        for i in get_invalid(start, end, exactly_twice=True)
    ]

    return sum(all_invalid_ids_list)


def day2_part2() -> int:
    start_end_tuple_list = get_input()

    all_invalid_ids_list = [
        i
        for start, end in start_end_tuple_list
        for i in get_invalid(start, end, exactly_twice=False)
    ]

    return sum(all_invalid_ids_list)
