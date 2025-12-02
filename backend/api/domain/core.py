from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class PaginationParams:
    """Domain model for Pagination Params"""

    page: int
    page_size: int


@dataclass
class ListingResult(Generic[T]):
    """Domain model representing a paginated listing result"""

    items: list[T]
    total_items: int
    total_pages: int
