from pathlib import Path


def get_input() -> list[tuple]:
    with Path("src/advent_of_code_2025/input9.txt").open() as file:
        data = file.read().strip().split("\n")

    return [tuple(int(x) for x in row.replace(")", "").split(",")) for row in data]


def get_area(point_1: tuple, point_2: tuple) -> int:
    x_dist = abs(point_1[0] - point_2[0]) + 1
    y_dist = abs(point_1[1] - point_2[1]) + 1

    return x_dist * y_dist


def cal_max_area(points_list: list[tuple]) -> int:
    max_area = 0
    working_points = points_list.copy()

    while working_points:
        point = working_points.pop()

        for other_point in working_points:
            area = get_area(point, other_point)
            max_area = max(max_area, area)

    return max_area


def day9_part1() -> int:
    points_list = get_input()
    return cal_max_area(points_list)
