/* eslint-disable no-var */
/**
 * @classdesc Book class
 * @constructor
 * @param {string} title book's title
 */
var Book = function Book(title) {
  /* eslint-disable no-underscore-dangle, no-var */
  var _title = title;
  /* eslint-enable no-underscore-dangle, no-var */

  Object.defineProperties(this, {
    title: {
      get: function get() {
        return _title;
      },
      set: function set(value) {
        if (typeof value !== 'string') return;
        _title = value;
      },
    },
  });
};

module.exports = Book;
