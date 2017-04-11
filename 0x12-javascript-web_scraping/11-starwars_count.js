#!/usr/bin/node
/*

Write a script that prints the number of movies where the character "Wedge Antilles" is present.

Requirements:
* The first argument is the API URL.
* Must use the Star Wars API (swapi.co) with the endpoint:
    http://swapi.co/api/films/

* Wedge Antilles is character ID is 18.

*/

const request = require('request');
var url = process.argv[2];
var count = 0;

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  let data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    let search = data[i].characters.find((name) => {
      return name.match(/18/);
    });
    if (search !== undefined) {
      count++;
    }
  }

  console.log(count);
});
