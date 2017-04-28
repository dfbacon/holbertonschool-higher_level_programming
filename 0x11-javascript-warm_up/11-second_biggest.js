#!/usr/bin/node
/*
Write a script that searches the second largest integer in
the list of arguments.

Requirements:
* You can assume all arguments can be converted to integer
* If no argument passed, print 0
* If the number of arguments is 1, print 0
* You must use console.log(...) to print all output
* You are not allowed to use var

*/

let argList = process.argv.slice(2).map((i) => {
  return parseInt(i);
});

if (argList.length <= 1) {
  console.log(0);
} else {
  console.log(argList.sort((a, b) => {
    return b - a;
  })[1]);
}
