from src.advent_of_code_2025.day9 import (
    calc_max_area,
    check_bounded,
    get_area,
)


def test_get_area() -> None:
    point_1 = (2, 5)
    point_2 = (11, 1)

    output_1 = get_area(point_1, point_2)
    output_2 = get_area(point_2, point_1)

    assert output_1 == output_2

    expected = 50

    assert output_1 == expected


def test_cal_max_area() -> None:
    input_data = [(7, 1), (11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3)]

    output = calc_max_area(input_data)

    expected = 50

    assert output == expected


def test_check_bounded() -> None:
    points_list = [(7, 1), (11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3)]

    bounded_point = (5, 4)
    unbounded_point = (1, 1)

    assert check_bounded(bounded_point, points_list) is True
    assert check_bounded(unbounded_point, points_list) is False


def test_calc_max_area_bounded() -> None:
    input_data = [(7, 1), (11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3)]

    output = calc_max_area(input_data, bounded=True)

    expected = 24

    assert output == expected
