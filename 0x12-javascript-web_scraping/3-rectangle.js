#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle.
* 3-main.js:
    #!/usr/bin/node
    const Rectangle = require('./3-rectangle').Rectangle;

    const r1 = new Rectangle(2, 3);
    r1.print();

    const r2 = new Rectangle(10, 5);
    r2.print();

Requirements:
* Must use the `function` notation for defining a class.
* Constructor must take 2 arguments: w and h.
* Initialize the instance attribute `width` with the value of w.
* Initialize the instance attribute `height` with the value of h.
* if w or h is 0 or negative, create empty object.
* Create instance method `print()` that prints the rectangle with an X.

*/

module.exports = {
  Rectangle: function (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      for (let x = 0; x < this.height; x++) {
        console.log(('X').repeat(this.width));
      }
    };
  }
};
