#!/usr/bin/node
/*

Write a script that writes a string to a file.

Requirements:
* The first argument is the file path.
* The second argument is the string to write.
* The content of the file must be read in `utf-8`.
* If an error occurres during writing, print the error object.

*/

const fs = require('fs');
var file = process.argv[2] || '';
var string = process.argv[3] || '';

fs.writeFile(file, string, (err) => {
  if (err) {
    return console.log(err);
  }
});
