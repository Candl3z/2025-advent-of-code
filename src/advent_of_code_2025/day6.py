import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def get_input() -> list[list[str]]:
    with Path("src/advent_of_code_2025/input6.txt").open() as f:
        data = f.read().strip()

    split_data = data.split("\n")
    split_data[-1] = split_data[-1] + " "  # ensure last line has a trailing space
    return split_data


def day6_part1() -> int:
    split_data = get_input()
    tableized_data = [[val for val in row.split(" ") if val != ""] for row in split_data]

    zipped_data = zip(
        tableized_data[0],
        tableized_data[1],
        tableized_data[2],
        tableized_data[3],
        tableized_data[4],
        strict=False,
    )

    totaled_list = [
        sum((int(val1), int(val2), int(val3), int(val4)))
        if op == "+"
        else int(val1) * int(val2) * int(val3) * int(val4)
        if op == "*"
        else 0
        for val1, val2, val3, val4, op in zipped_data
    ]

    return sum(totaled_list)


def get_sum_or_product(num_list: list[int], op: str) -> int:
    if op == "+":
        return sum(num_list)
    if op == "*":
        product = 1
        for n in num_list:
            product *= n
        return product
    raise ValueError(op)


def get_totaled_list(split_data: list[str]) -> list[int]:
    num_rows = len(split_data)

    tranposed_data = [
        tuple(split_data[i][col] for i in range(num_rows)) for col in range(len(split_data[0]))
    ]

    logger.debug("Transposed Data: %s", list(tranposed_data))

    op = ""
    short_list = []
    totaled_list = []

    for num in tranposed_data:
        striped_num = "".join(num).strip()

        if striped_num == "":
            totaled_list.append(get_sum_or_product(short_list, op))
            short_list = []
            continue

        if not short_list:
            op = striped_num[-1]
            striped_num = striped_num[:-1]

        short_list.append(int(striped_num))

    totaled_list.append(get_sum_or_product(short_list, op))

    return totaled_list


def day6_part2() -> int:
    split_data = get_input()

    totaled_list = get_totaled_list(split_data)

    return sum(totaled_list)
