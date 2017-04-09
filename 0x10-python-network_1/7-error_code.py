#!/usr/bin/python3
'''

This is the '7-error_code' module.

7-error_code takes in a URL, sends a request to the URL and displays the body
of the response.

Assignment Requirements:
* If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don't need to check arguments passed to the script (number or type)

Usage:
$ ./7-error_code.py domain_name

'''

if __name__ == "__main__":
