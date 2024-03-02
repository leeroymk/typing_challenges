import dataclasses
from typing import Mapping

from constants import ___


@dataclasses.dataclass()
class NameGender:
    client: Mapping[str, bool]


def is_name_male(name: str, name_gender_map: NameGender) -> bool | None:
    pass


if __name__ == "__main__":
    name_gender_map = NameGender(
        {
            "John": True,
            "Jane": False,
        }
    )
    assert is_name_male("John", name_gender_map) is True
    assert is_name_male("Unknown", name_gender_map) is None
