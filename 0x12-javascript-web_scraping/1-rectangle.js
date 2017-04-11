#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle.
* 1-main.js:
    #!/usr/bin/node
    const Rectangle = require('./1-rectangle').Rectangle;

    const r1 = new Rectangle(2, 3);
    console.log(r1);
    console.log(r1.width);
    console.log(r1.height);

    const r2 = new Rectangle(2, -3);
    console.log(r2);
    console.log(r2.width);
    console.log(r2.height);

    const r3 = new Rectangle(2);
    console.log(r3);
    console.log(r3.width);
    console.log(r3.height);

Requirements:
* Must use the `function` notation for defining a class.
* Constructor must take 2 arguments: w and h.
* Initialize the instance attribute `width` with the value of w.
* Initialize the instance attribute `height` with the value of h.

*/

module.exports = {
  Rectangle: function (w, h) {
    this.width = w;
    this.height = h;
  }
};
