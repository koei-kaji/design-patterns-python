/* eslint-disable no-var */

/**
 * Iterator Interface
 * @interface
 * @throws Error if constructor property is itself
 */
var IteratorIF = function IteratorIF() {
  if (this.constructor === IteratorIF) {
    throw new Error("Can't instantiate abstract class");
  }
};
IteratorIF.prototype = {
  /**
   * @abstract
   * @throws Error
   */
  hasNext: function hasNext() {
    throw new Error('Abstract method');
  },
  /**
   * @abstract
   * @throws Error
   */
  next: function next() {
    throw new Error('Abstract method');
  },
};

/**
 * Aggregate Interface
 * @interface
 * @throws Error if constructor property is itself
 */
var AggregateIF = function AggregateIF() {
  if (this.constructor === AggregateIF) {
    throw new Error("Can't instantiate abstract class");
  }
};
AggregateIF.prototype = {
  /**
   * @abstract
   * @throws Error
   */
  iterator: function iterator() {
    throw new Error('Abstract method');
  },
};

module.exports = {
  IteratorIF,
  AggregateIF,
};
