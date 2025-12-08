import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def get_pos_y(split_map: list[list[str]], beam_pos_y: int | None) -> int:
    if beam_pos_y is None:
        for row in split_map:
            if "S" in row:
                return split_map.index(row)
    return beam_pos_y


def get_pos_x(split_map: list[list[str]], beam_pos_x: int | None, beam_pos_y_int: int) -> int:
    return split_map[beam_pos_y_int].index("S") if beam_pos_x is None else beam_pos_x


def get_split_count(
    split_map: list[list[str]],
    beam_pos_y: int | None = None,
    beam_pos_x: int | None = None,
) -> int:
    beam_pos_y_int = get_pos_y(split_map, beam_pos_y)

    beam_pos_x_int = get_pos_x(split_map, beam_pos_x, beam_pos_y_int)

    if split_map[beam_pos_y_int][beam_pos_x_int] == "^":
        return 0

    split_map[beam_pos_y_int][beam_pos_x_int] = "|"

    logger.debug("Current Map State:\n%s", "\n".join("".join(row) for row in split_map))

    if len(split_map) == beam_pos_y_int + 1 or split_map[beam_pos_y_int + 1][beam_pos_x_int] == "|":
        return 0
    if split_map[beam_pos_y_int + 1][beam_pos_x_int] == ".":
        return get_split_count(split_map, beam_pos_y_int + 1, beam_pos_x_int)

    if split_map[beam_pos_y_int + 1][beam_pos_x_int] == "^":
        return (
            get_split_count(
                split_map,
                beam_pos_y_int + 1,
                beam_pos_x_int - 1,
            )
            + get_split_count(
                split_map,
                beam_pos_y_int + 1,
                beam_pos_x_int + 1,
            )
            + 1
        )

    raise ValueError(split_map[beam_pos_y_int + 1][beam_pos_x_int])


def get_path_count(
    split_map: list[list],
) -> int:
    for row_num in range(len(split_map)):
        row = split_map[row_num]

        if "S" in row:
            split_map[row_num][row.index("S")] = 1
            continue

        for col_num in range(len(row)):
            col_val = row[col_num]
            col_above = (
                0 if split_map[row_num - 1][col_num] == "^" else split_map[row_num - 1][col_num]
            )

            if col_val == "^":
                split_map[row_num][col_num - 1] += col_above
                split_map[row_num][col_num + 1] += col_above
            else:
                split_map[row_num][col_num] += col_above

    return sum(split_map[-1])


def get_input() -> list[list[str]]:
    with Path("src/advent_of_code_2025/input7.txt").open() as file:
        data = file.read().strip().split("\n")

    return [list(row) for row in data]


def day7_part1() -> int:
    split_data = get_input()

    return get_split_count(split_data)


def day7_part2() -> int:
    split_data = get_input()

    replace_with_zero = [[0 if col == "." else col for col in row] for row in split_data]

    return get_path_count(replace_with_zero)
