#!/usr/bin/node
/*
Write a function that returns the addition of 2 integers.

* 13-main.js
    #!/usr/bin/node
    const add = require('./13-add').add;
    console.log(add(3, 5));

Requirements:
* The function must be visible from outside
* The name of the function must be add
* You are not allowed to use var

*/

module.exports = {
  add: function (a, b) {
    return a + b;
  }
};
