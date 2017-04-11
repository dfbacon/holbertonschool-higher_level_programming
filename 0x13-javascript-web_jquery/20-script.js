/*

Write a Javascript script that updates the text of the HTML tag HEADER to "New Header!!!" when the user clicks on DIV#update_header.

* 20-main.html:

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
    <BR />
    <DIV id="update_header">Update the header</DIV>
    <BR />
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
    <SCRIPT type="text/javascript" src="20-script.js"></SCRIPT>
  </BODY>
 </HTML>

Requirements:
* You can't use `document.querySelector` to select the HTML tag
* You must use the jQuery API

*/

$('DIV#update_header').on('click', function () {
  $('header').html('New Header!!!');
});
