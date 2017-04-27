#!/usr/bin/node
/*
Write a script that prints the first argument passed to it.

Requirements:
* If no arguments are passed to the script, print "No argument".
* You must use console.log(...) to print all output
* You are not allowed to use var
* You are not allowed to use length

*/

const argOne = process.argv[2];
if (argOne === undefined) {
  console.log('No argument');
} else {
  console.log(argOne);
}
