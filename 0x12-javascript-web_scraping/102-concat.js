#!/usr/bin/node
/*

Write a script that concats 2 files.

Requirements:
* The first argument is the file path of the first source file.
* The second argument is the file path of the second source file.
* The third argument is the file path of the destination.

*/

let fs = require('fs');
let firstFile = process.argv.slice(2)[0];
let secondFile = process.argv.slice(2)[1];
let thirdFile = process.argv.slice(2)[2];

fs.readFile(firstFile, 'utf-8', function (error, data) {
  if (error) {
    return console.log(error);
  }
  fs.appendFileSync(thirdFile, data);
});

fs.readFile(secondFile, 'utf-8', function (error, data) {
  if (error) {
    return console.log(error);
  }
  fs.appendFileSync(thirdFile, data);
});
