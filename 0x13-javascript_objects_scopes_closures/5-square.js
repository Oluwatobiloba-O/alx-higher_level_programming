#!/usr/bin/node
//  class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  // a class Square that defines a square

  constructor (size) {
    super(size, size);
  }
};