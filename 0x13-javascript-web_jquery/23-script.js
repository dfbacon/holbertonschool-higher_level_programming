#!/usr/bin/node
/*

Write a Javascript script that fetches and prints the San Francisco wind speed by using this URL:
    * https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json

* 23-main.html:

 <!DOCTYPE html>
 <HTML lang="en">
  <HEAD>
    <TITLE>Holberton School</TITLE>
    <SCRIPT src="https://code.jquery.com/jquery-3.2.1.min.js"></SCRIPT>
    <SCRIPT type="text/javascript" src="23-script.js"></SCRIPT>
  </HEAD>
  <BODY>
    <HEADER>
      San Francisco - wind speed
    </HEADER>
    <BR />
    <DIV id="sf_wind_speed"></DIV>
    <BR />
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
  </BODY>
 </HTML>

Requirements:
* You can't use `document.querySelector` to select the HTML tag
* You must use the jQuery API
* All movie titles must be list in the HTML tag UL#list_movies

*/
const request = require('request');
const url = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json';

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  $('DIV#sf_wind_speed').text(JSON.parse(body).query.results.channel.wind.speed);
});
