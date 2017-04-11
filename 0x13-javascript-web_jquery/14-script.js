/*

Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000).

* 14-main.html:

 <!DOCTYPE html>
 <HTML lang="en">
  <HEAD>
    <TITLE>Holberton School</TITLE>
  </HEAD>
  <BODY>
    <HEADER>
      First HTML page
    </HEADER>
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
    <SCRIPT type="text/javascript" src="14-script.js"></SCRIPT>
  </BODY>
 </HTML>

Requirements:
* You must use `document.querySelector` to select the HTML tag
* You can't use the jQuery API

*/

let head = document.querySelector('header');

head.style.color = 'red';
