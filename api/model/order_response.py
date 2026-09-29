from dataclasses import dataclass


@dataclass
class Order:
    _id: str
    order_by_id: str
    order_by: str
    product_ordered_id: str
    product_name: str
    country: str
    product_description: str
    product_image: str
    order_date: str | None
    order_price: str
    __v: int


@dataclass
class OrderResponse:
    data: list[Order]
    count: int
    message: str