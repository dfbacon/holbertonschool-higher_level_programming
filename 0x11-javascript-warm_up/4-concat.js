#!/usr/bin/node
/*
Write a script that prints two arguments passed to it, in the
following format: " is ".

Requirements:
* You must use console.log(...) to print all output
* You are not allowed to use var

*/

const args = process.argv;
console.log(args[2] + ' is ' + args[3]);
