#!/usr/bin/node
/*
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using
an array of string and a loop.

Requirements:
* You must use console.log(...) to print all output
* You are not allowed to use var
* You are not allowed to use any if/else statements
* You are only allowed to use console.log one time
* You must use a loop

*/

const stringList = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (let i = 0; i < stringList.length; i++) {
  console.log(stringList[i]);
}
