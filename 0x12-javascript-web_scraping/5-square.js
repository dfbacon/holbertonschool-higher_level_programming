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

const Rectangle = require('./4-rectangle.js').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

exports.Rectangle = Rectangle;
exports.Square = Square;
