/*

Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header.

* 17-main.html:

 <!DOCTYPE html>
 <HTML lang="en">
  <HEAD>
    <TITLE>Holberton School</TITLE>
    <SCRIPT src="https://code.jquery.com/jquery-3.2.1.min.js"></SCRIPT>
    <STYLE>
      .red {
        color: #FF0000;
      }
    </STYLE>
  </HEAD>
  <BODY>
    <HEADER>
      First HTML page
    </HEADER>
    <DIV id="red_header">Red header</DIV>
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
    <SCRIPT type="text/javascript" src="17-script.js"></SCRIPT>
  </BODY>
 </HTML>

Requirements:
* You can't use `document.querySelector` to select the HTML tag
* You must use the jQuery API

*/

$('DIV#red_header').on('click', function () {
  $('header').addClass('red');
});
