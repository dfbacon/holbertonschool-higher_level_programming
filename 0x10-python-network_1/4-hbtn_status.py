#!/usr/bin/python3
'''

This is the '4-hbtn_status' module.

4-hbtn_status fetches a URL.

Assignment Requirements:
* You must use the package requests
* You are not allow to import packages other than requests
* The body of the response must be displayed in the specified format

Usage:
$ ./4-hbtn_status.py

'''

if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
