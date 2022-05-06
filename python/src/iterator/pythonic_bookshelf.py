from typing import Iterable, Iterator, List

from pydantic import BaseModel, PrivateAttr

from .book import Book


class PythonicBookShelf(BaseModel, Iterable[Book]):
    _books: List[Book] = PrivateAttr(default=[])
    _index: int = PrivateAttr(default=0)

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        self._books.append(book)

    def get_length(self) -> int:
        return len(self._books)

    def __iter__(self) -> Iterator[Book]:  # type: ignore[override]
        return self

    def __next__(self) -> Book:
        if self._index == len(self._books):
            raise StopIteration()
        book = self._books[self._index]
        self._index += 1

        return book
