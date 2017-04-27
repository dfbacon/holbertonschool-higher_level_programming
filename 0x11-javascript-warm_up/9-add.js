#!/usr/bin/node
/*
Write a script that prints the sum of 2 integers

Requirements:
* The first argument is the first integer.
* The second argument is the second integer.
* You have to define a function with this prototype:
    function add(a, b)

* You must use console.log(...) to print all output
* You are not allowed to use var
* You must use a loop

*/

const f = parseInt(process.argv[2]);
const s = parseInt(process.argv[3]);
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return;
  }
  return a + b;
}

console.log(add(f, s));
