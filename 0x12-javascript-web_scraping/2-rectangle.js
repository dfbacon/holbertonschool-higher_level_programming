#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle.
* 2-main.js:
    #!/usr/bin/node
    const Rectangle = require('./2-rectangle').Rectangle;

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

    const r4 = new Rectangle(2, 0);
    console.log(r4);
    console.log(r4.width);
    console.log(r4.height);

Requirements:
* Must use the `function` notation for defining a class.
* Constructor must take 2 arguments: w and h.
* Initialize the instance attribute `width` with the value of w.
* Initialize the instance attribute `height` with the value of h.
* if w or h is 0 or negative, create empty object.
*/

module.exports = {
  Rectangle: function (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
