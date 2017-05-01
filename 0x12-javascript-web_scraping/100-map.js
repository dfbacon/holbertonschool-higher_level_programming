#!/usr/bin/node
/*

Write a script that imports an array and computes a new array.

Requirements:
* Your script must import `list` from the file `100-data.js`.
* You must use a `map`.
* A new list must be created with each value, equal to the value of the initial list multiplied by the index in the list.
* Print both the initial list and the new list.

*/

let list = require('./100-data').list;

console.log(list);
list = list.map((i, j) => {
  return i * j;
});

console.log(list);
