/*

Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000).

* 15-main.html:

 <!DOCTYPE html>
 <HTML lang="en">
  <HEAD>
    <TITLE>Holberton School</TITLE>
    <SCRIPT src="https://code.jquery.com/jquery-3.2.1.min.js"></SCRIPT>
  </HEAD>
  <BODY>
    <HEADER>
      First HTML page
    </HEADER>
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
    <SCRIPT type="text/javascript" src="15-script.js"></SCRIPT>
  </BODY>
 </HTML>

Requirements:
* You can't use `document.querySelector` to select the HTML tag
* You must use the jQuery API

*/

$('header').css("color", "#FF0000")
