/**
 * Aggregate Interface
 * @export
 * @interface Aggregate
 */
export default class Aggregate {
  /**
   * Creates an instance of Aggregate.
   * @memberof Aggregate
   * @throws Error
   */
  constructor() {
    if (this === Aggregate) {
      throw new Error("Can't instantiate abstract class");
    }
  }

  /* eslint-disable class-methods-use-this */
  /**
   * @abstract
   * @memberof Aggregate
   * @throws Error
   */
  iterator() {
    throw new Error('Abstract method');
  }
  /* eslint-enable class-methods-use-this */
}
