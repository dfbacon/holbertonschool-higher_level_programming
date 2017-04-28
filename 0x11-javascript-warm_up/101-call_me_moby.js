#!/usr/bin/node
module.exports = {
  callMeMoby: function (i, f) {
    for (let x = 0; x < i; x++) {
      f();
    }
  }
};
