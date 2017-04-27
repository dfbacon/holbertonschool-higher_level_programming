#!/usr/bin/node
/*
Write a script that computes and prints a factorial.

Requirements:
* The first argument is integer used for computing the factorial
* Factorial of NaN is 1
* You must use a function
* You must use console.log(...) to print all output
* You are not allowed to use var

*/

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
