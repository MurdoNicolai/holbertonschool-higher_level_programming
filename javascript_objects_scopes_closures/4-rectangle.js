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

  /* Create an instance method called rotate() that exchanges the width and
the height of the rectangle */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /* Create an instance method called double() that multiples the width
and the height of the rectangle by 2 */
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
