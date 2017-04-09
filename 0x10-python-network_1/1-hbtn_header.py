#!/usr/bin/python3
'''

This is the '1-hbtn_header' module.

1-hbtn_header sends a request to a specifiec URL and displays the value of
X-Request_Id variable from the header of the response.

Assignment Requirements:
* You must use the packages urllib and sys
* You are not allow to import packages other than urllib and sys
* The value of this variable is different for each request
* You don't need to check arguments passed to the script (number or type)

Usage:
$ ./1-hbtn_header.py domain_name

'''

if __name__ == "__main__":
    import urllib.request
    import sys

    if len(sys.argv) < 2:
        print("Usage: ./1-hbtn_header.py domain_name")
        exit(1)

    url = sys.argv[1]
    page, header = urllib.request.urlretrieve(url)
    print(header['X-REQUEST-Id'])
