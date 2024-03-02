import dataclasses

from constants import ___


@dataclasses.dataclass()
class Coordinates:
    x: int
    y: int


def is_point_in_square(
    point: Coordinates,
    left_upper_corner: Coordinates,
    right_bottom_corner: Coordinates,
) -> bool:
    pass


if __name__ == "__main__":
    assert (
        is_point_in_square(
            point=Coordinates(10, 12),
            left_upper_corner=Coordinates(5, 5),
            right_bottom_corner=Coordinates(20, 15),
        )
        is True
    )
