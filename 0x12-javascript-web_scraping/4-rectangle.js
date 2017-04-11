#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle.
* 4-main.js:
    #!/usr/bin/node
    const Rectangle = require('./4-rectangle').Rectangle;

    const r1 = new Rectangle(2, 3);
    console.log('Normal:');
    r1.print();

    console.log('Double:');
    r1.double();
    r1.print();

    console.log('Rotate:');
    r1.rotate();
    r1.print();

Requirements:
* Must use the `function` notation for defining a class.
* Constructor must take 2 arguments: w and h.
* Initialize the instance attribute `width` with the value of w.
* Initialize the instance attribute `height` with the value of h.
* if w or h is 0 or negative, create empty object.
* Create instance method `print()` that prints the rectangle with an X.
* Create an instance method called `rotate()` that exchanges the width and the height of the rectangle.
* Create an instance method called `double()` that multiples the width and the height of the rectangle by 2.

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

    this.rotate = function () {
      [this.width, this.height] = [this.height, this.width];
    };

    this.double = function () {
      this.width *= 2;
      this.height *= 2;
    };
  }
};
