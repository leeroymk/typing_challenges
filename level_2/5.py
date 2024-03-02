import dataclasses

from constants import ___


@dataclasses.dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str


def get_current_user() -> User:
    pass


if __name__ == "__main__":
    assert get_current_user() == User("Ilya Lebedev", 33, "melevir@gmail.com")
