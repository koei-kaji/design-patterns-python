from __future__ import annotations

from typing import Any, List

from pydantic import PrivateAttr

from src.iterator.iterator import IteratorIF

from ..common.custom_pydantic.config import BaseConfig
from ..common.custom_pydantic.model import ABCModel
from .aggregate import AggregateIF
from .book import Book


class ExtendableBookShelf(ABCModel, AggregateIF):
    _books: List[Book] = PrivateAttr(default=[])

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        self._books.append(book)

    def get_length(self) -> int:
        return len(self._books)

    def iterator(self) -> ExtendableBookShelfIterator:
        return ExtendableBookShelfIterator(bookshelf=self)

    class Config(ABCModel.Config, BaseConfig):
        pass


class ExtendableBookShelfIterator(ABCModel, IteratorIF):
    _bookshelf: ExtendableBookShelf = PrivateAttr()
    _index: int = PrivateAttr(default=0)

    def __init__(self, bookshelf: ExtendableBookShelf, **data: Any):
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
