#!/usr/bin/node
/*

Write a Javascript script that fetches and replaces the name of this URL:
    * http://swapi.co/api/people/5/?format=json

* 21-main.html:

 <!DOCTYPE html>
 <HTML lang="en">
  <HEAD>
    <TITLE>Holberton School</TITLE>
    <SCRIPT src="https://code.jquery.com/jquery-3.2.1.min.js"></SCRIPT>
  </HEAD>
  <BODY>
    <HEADER>
      Star Wars character
    </HEADER>
    <BR />
    <DIV id="character"></DIV>
    <BR />
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
    <SCRIPT type="text/javascript" src="21-script.js"></SCRIPT>
  </BODY>
 </HTML>

Requirements:
* You can't use `document.querySelector` to select the HTML tag
* You must use the jQuery API
* The name must be display in the HTML tag DIV#character

*/
const request = require('request');
const url = 'http://swapi.co/api/people/5/?format=json';

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  $('DIV#character').text(JSON.parse(body).name);
});
