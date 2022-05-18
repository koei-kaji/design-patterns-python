from typing import Final, Iterable, List, cast

import pytest

from src.iterator.book import Book
from src.iterator.bookshelf import BookShelf
from src.iterator.extendable_bookshelf import ExtendableBookShelf
from src.iterator.iterator import IteratorIF
from src.iterator.pythonic_bookshelf import PythonicBookShelf

BOOKS: Final[List[str]] = [
    "Around the World in 80 Days",
    "Bible",
    "Cinderella",
    "Daddy-Long-Legs",
]


class TestBookshelfIterator:
    def test_normal(self) -> None:
        bookshelf = BookShelf(maxsize=len(BOOKS))
        for book in BOOKS:
            bookshelf.append_book(Book(name=book))

        count = 0
        bookshelf_iter: IteratorIF = bookshelf.iterator()
        while bookshelf_iter.has_next():
            bk: Book = cast(Book, bookshelf_iter.next())
            assert bk.name == BOOKS[count]
            count += 1

    @pytest.mark.parametrize("maxsize", [0, 1])
    def test_exc_value_error(self, maxsize: int) -> None:
        bookshelf_holds_nothing = BookShelf(maxsize=maxsize)
        for i in range(maxsize):
            bookshelf_holds_nothing.append_book(Book(name=f"{BOOKS[i]}"))

        with pytest.raises(ValueError):
            bookshelf_holds_nothing.append_book(Book(name=f"{BOOKS[maxsize]}"))


class TestExtendableBookshelfIterator:
    def test_normal(self) -> None:
        bookshelf = ExtendableBookShelf()
        for book in BOOKS:
            bookshelf.append_book(Book(name=book))

        count = 0
        bookshelf_iter: IteratorIF = bookshelf.iterator()
        while bookshelf_iter.has_next():
            bk: Book = cast(Book, bookshelf_iter.next())
            assert bk.name == BOOKS[count]
            count += 1


class TestPythonicBookShelf:
    def test_normal(self) -> None:
        bookshelf = PythonicBookShelf()
        for book in BOOKS:
            bookshelf.append_book(Book(name=book))

        assert iter(bookshelf) is not None
        assert isinstance(bookshelf, Iterable) is True
        for i, bk in enumerate(bookshelf):
            assert bk.name == BOOKS[i]
