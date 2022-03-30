from __future__ import annotations

from typing import Any, List

from pydantic import PrivateAttr

from ..common.custom_pydantic import BaseConfig
from .aggregate import AggregateABC
from .book import Book
from .iterator import IteratorABC


class BookShelf(AggregateABC):
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

    class Config(BaseConfig):
        pass


class BookShelfIterator(IteratorABC):
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

    class Config(BaseConfig):
        pass
