#!/usr/bin/node
/*

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

Requirements:
* The first argument is the episode number.
* Must use the Star Wars API (swapi.co) with the endpoint:
    http://swapi.co/api/films/:episode_id

*/

const request = require('request');
const id = parseInt(process.argv[2]);
const url = 'http://swapi.co/api/films/' + id;

if (id < 8) {
  request(url, function (error, response, body) {
    if (error) {
      return console.log(error);
    }

    console.log(JSON.parse(body).title);
  });
}
