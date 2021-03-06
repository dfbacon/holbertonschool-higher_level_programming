#!/usr/bin/python3
'''

This is the '5-hbtn_header.py' module.

5-hbtn_header takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header.

Assignment Requirements:
* You must use the packages requests and sys
* You are not allow to import other packages than requests and sys
* The value of this variable is different for each request
* You don't need to check script arguments (number and type)

Usage:
$ ./5-hbtn_header domain_name

'''

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py domain_name")
        exit(1)

    try:
        url = sys.argv[1]
        r = requests.get(url)
        print("{}".format(r.headers['X-Request-Id']))
    except:
        pass
