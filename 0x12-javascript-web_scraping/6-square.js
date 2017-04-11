#!/usr/bin/node
/*
Write a class `Square` that defines a square and inherits from `Square` of 5-square.js
* 6-main.js:
    #!/usr/bin/node
    const Square = require('./6-square').Square;

    const s1 = new Square(4);
    s1.charPrint();

    s1.charPrint('C');

Requirements:
* You must use the `prototype` notation for adding new method.
* Create an instance method called `charPrint(c)` that prints using the character c.
    * If c is undefined, default to X

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

Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    for (let x = 0; x < this.height; x++) {
      console.log(('X').repeat(this.width));
    }
  } else {
    for (let x = 0; x < this.height; x++) {
      console.log((c).repeat(this.width));
    }
  }
};

exports.Rectangle = Rectangle;
exports.Square = Square;
