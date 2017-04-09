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

    r = urllib.request.Request('https://intranet.hbtn.io/status', data)
    with urllib.request.urlopen(r) as response:
        html = response.read()
        print(html)
