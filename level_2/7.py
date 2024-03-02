import dataclasses

from constants import ___


@dataclasses.dataclass()
class User:
    name: str
    age: int
    student_learning_time: list[int]


def calculate_total_spent_for_user(user: User) -> int:
    pass


if __name__ == "__main__":
    assert (
        calculate_total_spent_for_user(user=User("Ilya", 32, [102, 15, 63, 12])) == 192
    )
