#!/usr/bin/node
/*

Write a script that reads and prints the content of a file.

Requirements:
* The first argument is the file path.
* The content of the file must be read in `utf-8`.
* If an error occurres during reading, print the error object.

*/

const fs = require('fs');

var file = process.argv[2] || '';
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(data);
});
