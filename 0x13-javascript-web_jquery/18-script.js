/*

Write a Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header.

* 18-main.html:

 <!DOCTYPE html>
 <HTML lang="en">
  <HEAD>
    <TITLE>Holberton School</TITLE>
    <SCRIPT src="https://code.jquery.com/jquery-3.2.1.min.js"></SCRIPT>
    <STYLE>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </STYLE>
  </HEAD>
  <BODY>
    <HEADER>
      First HTML page
    </HEADER>
    <DIV id="toggle_header">Toggle header</DIV>
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
    <SCRIPT type="text/javascript" src="18-script.js"></SCRIPT>
  </BODY>
 </HTML>

Requirements:
* You can't use `document.querySelector` to select the HTML tag
* You must use the jQuery API

*/

$('DIV#toggle_header').on('click', function () {
  $('header').toggleClass(function () {
    if ($(this).hasClass('red')) {
      return 'green';
    } else {
      return 'red';
    }
  });
});
