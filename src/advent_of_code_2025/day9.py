from pathlib import Path


def get_input() -> list[tuple]:
    with Path("src/advent_of_code_2025/input9.txt").open() as file:
        data = file.read().strip().split("\n")

    return [tuple(int(x) for x in row.replace(")", "").split(",")) for row in data]


def get_area(point_1: tuple, point_2: tuple) -> int:
    x_dist = abs(point_1[0] - point_2[0]) + 1
    y_dist = abs(point_1[1] - point_2[1]) + 1

    return x_dist * y_dist


def get_tangents(point_1: tuple, point_2: tuple) -> list[tuple]:
    tangents = []

    if point_1[0] == point_2[0] or point_1[1] == point_2[1]:
        return tangents

    tangents.append((point_1[0], point_2[1]))
    tangents.append((point_2[0], point_1[1]))

    return tangents


def check_bounded(point: tuple, points_list: list[tuple]) -> bool:
    for current_point, next_point in zip(
        points_list,
        points_list[1:] + points_list[:1],
        strict=True,
    ):
        if point in points_list:
            return True
        if current_point[0] == next_point[0]:
            if next_point[1] > current_point[1]:
                if current_point[0] < point[0] and current_point[1] <= point[1] <= next_point[1]:
                    return False
            elif current_point[0] > point[0] and next_point[1] <= point[1] <= current_point[1]:
                return False
        elif next_point[0] > current_point[0]:
            if current_point[1] > point[1] and current_point[0] <= point[0] <= next_point[0]:
                return False
        elif current_point[1] < point[1] and next_point[0] <= point[0] <= current_point[0]:
            return False

    return True


def valid_area(point_1: tuple, point_2: tuple, points_list: list[tuple]) -> bool:
    return all(check_bounded(tangent, points_list) for tangent in get_tangents(point_1, point_2))


def calc_max_area(points_list: list[tuple], *, bounded: bool = False) -> int:
    max_area = 0
    working_points = points_list.copy()

    while working_points:
        point = working_points.pop()

        for other_point in working_points:
            if bounded and not valid_area(point, other_point, points_list):
                continue

            area = get_area(point, other_point)
            max_area = max(max_area, area)

    return max_area


def day9_part1() -> int:
    points_list = get_input()
    return calc_max_area(points_list)


def day9_part2() -> int:
    points_list = get_input()
    return calc_max_area(points_list, bounded=True)
