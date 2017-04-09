#!/usr/bin/python3
'''

This is the '8-json_api' module.

8-json_api takes in a letter and sends a POST request to a given domain name
with the letter as a parameter.

Assignment Requirements:
* The letter must be sent in the variable q
* If no argument is given, set q=""
* If the response body is properly JSON formatted and not empty, display the
id and name like this: [<id>] <name>
* Otherwise:
    * Display Not a valid JSON is the JSON is invalid
    * Display No result is the JSON is empty
* You must use the package requests and sys
* You are not allowed to import packages other than requests and sys

Usage:
$ ./8-json_api.py

'''

if __name__ == "__main__":
    import requests
    import sys

    try:
        l = sys.argv[1]
    except:
        l = ""

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": l}).json()
    if r = {}:
        print("No result")
    else:
        print("[{}] {}".format(r['id'], r['name']))
