#!/usr/bin/node
/*
Write a function that increments and calls a function.

* 102-main.js
    #!/usr/bin/node
    const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
    addMeMaybe(4, function (nb) {
      console.log('New value: ' + nb);
    });

Requirements:
* The function must be visible from outside.
* Prototype:
    function(number, theFunction)
* You are not allowed to use var

*/

module.exports = {
  addMeMaybe: function (n, f) {
    return f(n + 1);
  }
};
