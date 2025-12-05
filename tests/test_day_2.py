import pytest
from src.advent_of_code_2025.day2 import check_invalid, get_invalid


@pytest.mark.parametrize(
    ("check_num", "expected_out", "exactly_twice"),
    [
        (11, True, True),
        (13, False, True),
        (22, True, True),
        (1188511885, True, True),
        (118851188, False, True),
        (38593859, True, True),
        (123456789, False, True),
        (824824824, True, False),
        (824824825, False, False),
    ],
)
def test_check_invalid(check_num: int, *, expected_out: bool, exactly_twice: bool) -> None:
    assert check_invalid(check_num, exactly_twice=exactly_twice) == expected_out


@pytest.mark.parametrize(
    ("start", "end", "expected_out"),
    [(11, 22, [11, 22]), (95, 115, [99]), (998, 1012, [1010]), (38593856, 38593862, [38593859])],
)
def test_get_invalid(start: int, end: int, expected_out: list[int]) -> None:
    assert get_invalid(start, end) == expected_out
