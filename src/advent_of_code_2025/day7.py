import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def get_split_count(
    split_map: list[list[str]],
    beam_pos_y: int | None = None,
    beam_pos_x: int | None = None,
) -> int:
    if beam_pos_y is None:
        for row in split_map:
            if "S" in row:
                beam_pos_y_int = split_map.index(row)
                break
    else:
        beam_pos_y_int = beam_pos_y

    beam_pos_x_int = split_map[beam_pos_y_int].index("S") if beam_pos_x is None else beam_pos_x

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


def get_input() -> list[list[str]]:
    with Path("src/advent_of_code_2025/input7.txt").open() as file:
        data = file.read().strip().split("\n")

    return [list(row) for row in data]


def day7_part1() -> int:
    split_data = get_input()

    return get_split_count(split_data)
