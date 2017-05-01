#!/usr/bin/node
/*

Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

Requirements:
* Your script must import `dict` from the file `101-data.js`.
* The new dictionary must contain:
    * A key; the number of occurrences.
    * A value; the list of user ids.
* Print the new dictionary at the end.

*/

let dict = require('./101-data').dict;
let temp = {};

for (let instance in dict) {
  if (!temp[dict[instance]]) {
    temp[dict[instance]] = [];
  }

  temp[dict[instance]].push(instance);
}

console.log(temp);
