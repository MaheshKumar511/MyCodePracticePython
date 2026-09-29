from dataclasses import dataclass


@dataclass
class Product:
    _id: str
    product_name: str
    product_category: str
    product_sub_category: str
    product_price: int
    product_description: str
    product_image: str
    product_rating: str
    product_total_price: int | None = None
    product_total_orders: str | None = None
    product_status: bool | None = None
    product_for: str | None = None
    product_added_by: str | None = None
    __v: int | None = None


@dataclass
class ProductResponse:
    message: str
    data: list[Product]


@dataclass
class ProductDetailsResponse:
    message: str
    data: Product