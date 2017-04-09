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
    import urllib.request
    import urllib.parse
    import sys

    if len(sys.argv) < 3:
        print("Usage: ./2-post_email.py domain_name email_address")
        exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        address = (response.read()).decode('utf-8')
        print(address)
