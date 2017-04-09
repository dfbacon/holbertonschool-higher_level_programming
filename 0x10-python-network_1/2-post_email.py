#!/usr/bin/python3
'''

This is the '2-post_email.py' module.

2-post_email takes a URL and email and sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8).

Assignment Requirements:
* The email must be sent in the email variable
* You must use the packages urllib and sys
* You are not allowed to import packages other than urllib and sys
* You don't need to check arguments passed to the script (number or type)
* You must use the with statement

Usage:
$ ./2-post_email.py domain_name email_address

'''

if __name__ == "__main__":
