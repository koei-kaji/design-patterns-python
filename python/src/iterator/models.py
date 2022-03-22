from __future__ import annotations

import abc
from typing import Any, List

from pydantic import BaseModel, PrivateAttr


class IteratorIF(BaseModel, abc.ABC):
    @abc.abstractmethod
    def has_next(self) -> bool:
        pass

    @abc.abstractmethod
    def next(self) -> object:
        pass


class AggregateIF(BaseModel, abc.ABC):
    @abc.abstractmethod
    def iterator(self) -> IteratorIF:
        pass


class Book(BaseModel):
    name: str

    class Config:
        allow_mutation = False


class BookShelf(AggregateIF):
    _books: List[Book] = PrivateAttr(default=[])
    _last: int = PrivateAttr(default=0)
    _maxsize: int = PrivateAttr()

    def __init__(self, maxsize: int, **data: Any) -> None:
        super().__init__(**data)
        self._maxsize = maxsize

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        if len(self._books) == self._maxsize:
            raise ValueError("bookshelf is already full.")
        self._books.append(book)
        self._last += 1

    def get_length(self) -> int:
        return self._last

    def iterator(self) -> BookShelfIterator:
        return BookShelfIterator(self)


class ExtendableBookShelf(AggregateIF):
    _books: List[Book] = PrivateAttr(default=[])

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        self._books.append(book)

    def get_length(self) -> int:
        return len(self._books)

    def iterator(self) -> ExtendableBookShelfIterator:
        return ExtendableBookShelfIterator(self)


class BookShelfIterator(IteratorIF):
    _bookshelf: BookShelf = PrivateAttr()
    _index: int = PrivateAttr(default=0)

    def __init__(self, bookshelf: BookShelf, **data: Any):
        super().__init__(**data)
        self._bookshelf = bookshelf

    def has_next(self) -> bool:
        return self._index < self._bookshelf.get_length()

    def next(self) -> Book:
        book = self._bookshelf.get_book_at(self._index)
        self._index += 1

        return book


class ExtendableBookShelfIterator(IteratorIF):
    _bookshelf: ExtendableBookShelf = PrivateAttr()
    _index: int = PrivateAttr(default=0)

    def __init__(self, bookshelf: ExtendableBookShelf, **data: Any):
        super().__init__(**data)
        self._bookshelf = bookshelf

    def has_next(self) -> bool:
        return self._index < self._bookshelf.get_length()

    def next(self) -> Book:
        book = self._bookshelf.get_book_at(self._index)
        self._index += 1

        return book
