/* eslint-disable max-classes-per-file */
import Iterator from './iterator.mjs';

/**
 * BookShelfIterator
 * @export
 * @class BookShelfIterator
 * @extends {Iterator} iterator
 */
export default class BookShelfIterator extends Iterator {
  /* eslint-disable no-underscore-dangle */
  /**
   * Creates an instance of BookShelfIterator.
   * @param {BookShelf} bookshelf
   * @memberof BookShelfIterator
   */
  constructor(bookshelf) {
    super();
    this._bookshelf = bookshelf;
  }

  get bookshelf() {
    return this._bookshelf;
  }

  get index() {
    return this._index;
  }

  set index(value) {
    if (typeof value !== 'number') return;
    this._index = value;
  }

  /**
   * Returns the boolean if has next or not
   * @return {boolean} if has next or not
   * @memberof BookShelfIterator
   */
  hasNext() {
    return this._index < this._bookshelf.getLength();
  }

  /**
   * Returns next book and count up index
   * @return {Book} Book
   * @memberof BookShelfIterator
   */
  next() {
    const bk = this._bookshelf.getBookAt(this._index);
    this._index += 1;

    return bk;
  }

  /* eslint-enable no-underscore-dangle */
}
