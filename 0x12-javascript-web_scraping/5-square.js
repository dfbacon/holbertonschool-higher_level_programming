#!/usr/bin/node
/*
Write a class `Square` that defines a square and inherits from `Rectangle` of 4-rectangle.js
* 5-main.js:
    #!/usr/bin/node
    const Square = require('./5-square').Square;

    const s1 = new Square(4);
    s1.print();
    s1.double();
    s1.print();

Requirements:
* Must use the `function` notation for defining a class.
* Constructor must take 1 argument: size.
* Constructor `Rectangle` must be called.

*/

function Rectangle (w, h) {
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

function Square (size) {
  Rectangle.call(this, size, size);
}

exports.Rectangle = Rectangle;
exports.Square = Square;
