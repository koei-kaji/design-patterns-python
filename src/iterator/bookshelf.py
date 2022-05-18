from __future__ import annotations

from typing import Any, List

from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseConfig
from ..common.custom_pydantic.model import ABCModel
from .aggregate import AggregateIF
from .book import Book
from .iterator import IteratorIF


class BookShelf(ABCModel, AggregateIF):
    _books: List[Book] = PrivateAttr(default=[])
    _maxsize: int = PrivateAttr()

    def __init__(self, maxsize: int, **data: Any) -> None:
        super().__init__(**data)
        self._maxsize = maxsize

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        if len(self._books) >= self._maxsize:
            raise ValueError("bookshelf is already full.")
        self._books.append(book)

    def get_length(self) -> int:
        return len(self._books)

    def iterator(self) -> BookShelfIterator:
        return BookShelfIterator(bookshelf=self)

    class Config(ABCModel.Config, BaseConfig):
        pass


class BookShelfIterator(ABCModel, IteratorIF):
    _bookshelf: BookShelf = PrivateAttr()
    _index: int = PrivateAttr(default=0)

    def __init__(self, bookshelf: BookShelf, **data: Any):
        super().__init__(**data)
        self._bookshelf = bookshelf

    def has_next(self) -> bool:
        return self._index < self._bookshelf.get_length()

    def next(self) -> object:
        book = self._bookshelf.get_book_at(self._index)
        self._index += 1

        return book

    class Config(ABCModel.Config, BaseConfig):
        pass
