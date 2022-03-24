/**
 * Iterator Interface
 * @interface Iterator
 * @exports
 */
export default class Iterator {
  /**
   * Creates an instance of Iterator.
   * @memberof Iterator
   * @throws Error
   */
  constructor() {
    if (this === Iterator) {
      throw new Error("Can't instantiate abstract class");
    }
  }

  /* eslint-disable class-methods-use-this */
  /**
   * @abstract
   * @memberof Iterator
   * @throws Error
   */
  hasNext() {
    throw new Error('Abstract method');
  }

  /**
   * @abstract
   * @memberof Iterator
   * @throws Error
   */
  next() {
    throw new Error('Abstract method');
  }
  /* eslint-enable class-methods-use-this */
}
