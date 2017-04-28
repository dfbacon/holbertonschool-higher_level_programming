#!/usr/bin/node
/*
Write a function that executes x times a function.

* 101-main.js
    #!/usr/bin/node
    const callMeMoby = require('./101-call_me_moby').callMeMoby;
    callMeMoby(3, function () {
      console.log('C is fun');
    });

Requirements:
* The function must be visible from outside.
* Prototype:
    function (x, theFunction)

* You are not allowed to use var

*/

module.exports = {
  callMeMoby: function (i, f) {
    for (let x = 0; x < i; x++) {
      f();
    }
  }
};
