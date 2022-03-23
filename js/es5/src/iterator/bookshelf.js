/* eslint-disable no-var */
var interfaces = require('./interfaces');
var book = require('./book');

/**
 * @constructor
 * @augments interfaces.AggregateIF
 * @param {number} maxsize bookshelf's max size
 */
var BookShelf = function BookShelf(maxsize) {
  /* eslint-disable no-underscore-dangle */
  var _books = [];
  var _last = 0;
  var _maxsize = maxsize;
  /* eslint-enable no-underscore-dangle */

  interfaces.AggregateIF.call(this);

  Object.defineProperties(this, {
    books: {
      get: function get() {
        return _books;
      },
    },
    last: {
      get: function get() {
        return _last;
      },
      set: function set(value) {
        if (typeof value !== 'number') return;
        _last = value;
      },
    },
    maxsize: {
      get: function get() {
        return _maxsize;
      },
    },
  });
};
BookShelf.prototype = new interfaces.AggregateIF();
BookShelf.prototype.constructor = BookShelf;
/**
 * Returns book by index
 * @param {number} index
 * @returns {undefined|book.Book} book
 */
BookShelf.prototype.getBookAt = function getBookAt(index) {
  if (typeof index !== 'number') return undefined;
  if (this.books.length <= index) return undefined;
  return this.books[index];
};
/**
 * Append the book
 * @param {book.Book} bk book
 */
BookShelf.prototype.appendBook = function appendBook(bk) {
  // TODO: throw error the bookshelf is filled
  if (bk.constructor !== book.Book) return;
  this.books.push(bk);
};
/**
 * Returns the number of books filled in the bookshelf
 * @returns {number} the number of books
 */
BookShelf.prototype.getLength = function getLength() {
  return this.books.length;
};
/**
 * Returns the iterator
 * @returns {interfaces.IteratorIF} iterator
 */
BookShelf.prototype.iterator = function iterator() {
  // eslint-disable-next-line no-use-before-define
  return new BookShelfIterator(this);
};

var BookShelfIterator = function BookShelfIterator(bookshelf) {
  /* eslint-disable no-underscore-dangle */
  var _bookshelf = bookshelf;
  var _index = 0;
  /* eslint-enable no-underscore-dangle */

  Object.defineProperties(this, {
    bookshelf: {
      get: function get() {
        return _bookshelf;
      },
    },
    index: {
      get: function get() {
        return _index;
      },
      set: function set(value) {
        if (typeof value !== 'number') return;
        _index = value;
      },
    },
  });
};
BookShelfIterator.prototype = new interfaces.IteratorIF();
BookShelfIterator.prototype.constructor = BookShelfIterator;
/**
 * Returns the boolean if has next or not
 * @returns {boolean} if has next or not
 */
BookShelfIterator.prototype.hasNext = function hasNext() {
  return this.index < this.bookshelf.getLength();
};
/**
 * Returns next book and count up index
 * @returns {book.Book} book
 */
BookShelfIterator.prototype.next = function next() {
  // eslint-disable-next-line no-var
  var bk = this.bookshelf.getBookAt(this.index);
  this.index += 1;

  return bk;
};

module.exports = {
  BookShelf,
  BookShelfIterator,
};
