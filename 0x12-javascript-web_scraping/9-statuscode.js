#!/usr/bin/node
/*

Write a script that displays the status code of a `GET` request.

Requirements:
* The first argument is the URL to request.
* The status code must be printed like this:
    code: <status code>

*/

const request = require('request');
const url = process.argv[2] || '';

request(url, function (error, response) {
  if (error) {
    return console.log(error);
  }
  return console.log('code: ', response.statusCode);
});
