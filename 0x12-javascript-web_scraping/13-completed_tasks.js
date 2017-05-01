#!/usr/bin/node
/*

Write a script that computes the number of tasks completed by user id.

Requirements:
* The first argument is the API URL.
    https://jsonplaceholder.typicode.com/todos

*/

const request = require('request');
const url = process.argv[2] || '';
const completed = {};

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  let data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    let id = data[i].userId;
    if (data[i].completed) {
      completed[id] = (completed[id] || 0) + 1;
    }
  }

  console.log(completed);
});
