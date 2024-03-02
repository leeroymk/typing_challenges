import dataclasses
import datetime

from constants import ___


@dataclasses.dataclass()
class Order:
    goods: str
    quantity: int
    price: float


@dataclasses.dataclass()
class Receipt:
    order_id: int
    payment_date: datetime.date
    order: list[Order]


def parse_receipt(
    raw_receipt: str,
) -> Receipt:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == Receipt(12, datetime.date(2022, 6, 12), [Order("Молоко", 1, 32.2)])
