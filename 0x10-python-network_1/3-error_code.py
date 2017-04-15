#!/usr/bin/python3
'''

This is the '3-error_code' module.

3-error code takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).

Assignment Requirements:
* You have to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
* You must use the packages urllib and sys
* You are not allowed to import other packages than urllib and sys
* You don't need to check arguments passed to the script (number or type)
* You must use the with statement

Usage:
$ ./3-error_code.py domain_name

'''

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py domain_name")
        exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            page = (response.read()).decode('utf-8')
            print(page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code)
