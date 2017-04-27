#!/usr/bin/node
/*
Write a script that prints "My number: " if the first argument
can be converted to an integer.

Requirements:
* If the argument can't be converted to an integer, print "Not a number"
* You must use console.log(...) to print all output
* You are not allowed to use var
* You are not allowed to use try/catch

*/

const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
