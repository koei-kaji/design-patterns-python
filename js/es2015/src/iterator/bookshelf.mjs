import Aggregate from './aggregate.mjs';
import Book from './book.mjs';
import BookShelfIterator from './bookshelf_iterator.mjs';

export default class BookShelf extends Aggregate {
  /* eslint-disable no-underscore-dangle */
  constructor(maxsize) {
    super();
    this._books = [];
    this._last = 0;
    this._maxsize = maxsize;
  }

  get books() {
    return this._books;
  }

  get last() {
    return this._last;
  }

  set last(value) {
    if (typeof value !== 'number') return;
    this._last = value;
  }

  get maxsize() {
    return this._maxsize;
  }

  getBookAt(index) {
    if (typeof index !== 'number') return undefined;
    if (this._books.length <= index) return undefined;
    return this._books[index];
  }

  getLength() {
    return this._books.length;
  }

  appendBook(bk) {
    if (bk.constuctor !== Book) return;
    this._books.push(bk);
  }

  iterator() {
    return new BookShelfIterator(this);
  }
  /* eslint-enable no-underscore-dangle */
}
