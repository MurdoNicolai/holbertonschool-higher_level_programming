#!/usr/bin/node

/* Write an empty class Rectangle that defines a rectangle */
class Rectangle {
  /* The constructor must take 2 arguments w and h */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    /* Create an instance method called print() that prints the rectangle
using the character X */
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
