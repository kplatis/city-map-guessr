"""Defines Pydantic schemas for core functionalities like pagination."""

from typing import Generic, TypeVar

from pydantic import BaseModel

from api.domain.core import PaginationParams

T = TypeVar("T")


class PaginationParamsIn(BaseModel):
    """Pydantic model representing pagination parameters."""

    page: int = 1
    page_size: int = 10

    def to_domain(self) -> PaginationParams:
        """Convert pagination params to domain model."""

        return PaginationParams(page=self.page, page_size=self.page_size)


class PaginationInfoOut(BaseModel):
    """Pydantic model representing pagination information."""

    page: int
    page_size: int
    total_items: int
    total_pages: int


class PaginatedResponse(BaseModel, Generic[T]):
    """Pydantic model representing a paginated response."""

    items: list[T]
    pagination: PaginationInfoOut
    pagination: PaginationInfoOut
