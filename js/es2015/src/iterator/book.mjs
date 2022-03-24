/**
 * Book
 * @export
 * @class Book
 */
export default class Book {
  /* eslint-disable no-underscore-dangle */
  /**
   * Creates an instance of Book.
   * @param {string} title book's title
   * @memberof Book
   */
  constructor(title) {
    this.title = title;
  }

  /**
   * get title
   * @memberof Book
   */
  get title() {
    return this._title;
  }

  /**
   * set title
   * @param {string} title book's title
   * @memberof Book
   */
  set title(title) {
    if (typeof title !== 'string') return;
    this._title = title;
  }
  /** eslint-enable no-underscore-dangle */
}
