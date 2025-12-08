from textwrap import dedent

from src.advent_of_code_2025.day7 import get_path_count, get_split_count


def test_get_split_count() -> None:
    input_string = """
    .......S.......
    ...............
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    """

    input_string = dedent(input_string)

    input_lines = [list(row) for row in input_string.strip().split("\n")]

    output = get_split_count(input_lines)

    expected = 21

    assert output == expected


def test_get_split_count_single_path() -> None:
    input_string = """
    0000000S0000000
    000000000000000
    0000000^0000000
    000000000000000
    000000^0^000000
    000000000000000
    00000^0^0^00000
    000000000000000
    0000^0^000^0000
    000000000000000
    000^0^000^0^000
    000000000000000
    00^000^00000^00
    000000000000000
    0^0^0^0^0^000^0
    000000000000000
    """

    input_string = dedent(input_string)

    input_lines = [list(row) for row in input_string.strip().split("\n")]

    replace_with_zero = [[0 if col == "0" else col for col in row] for row in input_lines]

    output = get_path_count(replace_with_zero)
    expected = 40

    assert output == expected
