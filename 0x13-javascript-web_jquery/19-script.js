/*

Write a Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item.

* 19-main.html:

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
    <DIV id="add_item">Add item</DIV>
    <BR />
    <UL class="my_list">
      <LI>Item</LI>
    </UL>
    <FOOTER>
      Holberton School - 2017
    </FOOTER>
    <SCRIPT type="text/javascript" src="19-script.js"></SCRIPT>
  </BODY>
 </HTML>

Requirements:
* You can't use `document.querySelector` to select the HTML tag
* You must use the jQuery API
* The new element must be: <LI>Item</LI>
* The new element must be added to UL.my_list

*/

$('DIV#add_item').on('click', function () {
  $('UL.my_list').append('<LI>Item</LI>');
});
