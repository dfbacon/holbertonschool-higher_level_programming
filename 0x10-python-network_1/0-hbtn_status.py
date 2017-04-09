#!/usr/bin/python3
'''

This is the '0-hbtn_status module.

0-hbtn_status uses the urllib package to fetch data from a given domain name.

Assignment Requirements:
* You must use the package urllib
* You are not allowed to import any packages other than urllib
* The body of the response must be displayed in specified format
* You must use a with statement

Usage:
$ ./0-hbtn_status.py

'''

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
