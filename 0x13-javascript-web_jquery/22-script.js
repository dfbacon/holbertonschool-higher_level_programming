#!/usr/bin/node
/*

Write a Javascript script that fetches and lists all movie titles of this URL:
    * http://swapi.co/api/films?format=json

* 22-main.html:

 <!DOCTYPE html>
 <HTML lang="en">
  <HEAD>
    <TITLE>Holberton School</TITLE>
    <SCRIPT src="https://code.jquery.com/jquery-3.2.1.min.js"></SCRIPT>
  </HEAD>
  <BODY>
    <HEADER>
      Star Wars movies
    </HEADER>
    <BR />
    <UL id="list_movies">
    </UL>
    <BR />
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
    <SCRIPT type="text/javascript" src="22-script.js"></SCRIPT>
  </BODY>
 </HTML>

Requirements:
* You can't use `document.querySelector` to select the HTML tag
* You must use the jQuery API
* All movie titles must be list in the HTML tag UL#list_movies

*/
const request = require('request');
const url = 'http://swapi.co/api/people/5/?format=json';

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  let data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    $('UL#list_movies').append(data[i].title);
  }
});
