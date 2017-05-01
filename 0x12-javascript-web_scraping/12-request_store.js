#!/usr/bin/node
/*

Write a script that gets the contents of a webpage and stores it in a file.

Requirements:
* The first argument is the URL to request.
* The second argument is the file path to store the body response.
* The file must be UTF-8 encoded.

*/

const fs = require('fs');
const request = require('request');
const url = process.argv[2] || '';
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  fs.writeFile(file, body, 'utf8', function (error) {
    if (error) {
      return console.log(error);
    }
  });
});
