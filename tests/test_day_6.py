from src.advent_of_code_2025.day6 import get_totaled_list


def test_part_2() -> None:
    output = get_totaled_list(
        [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ],
    )

    expected = [8544, 625, 3253600, 1058]

    assert output == expected
