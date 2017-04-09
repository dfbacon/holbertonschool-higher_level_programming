#!/usr/bin/python3
'''

This is the '6-post_email' module.

6-post_email takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body of
the response.

Assignment Requirements:
* The email must be sent in the variable email
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don't need to error check arguments passed to the script (number or type)

Usage:
$ ./6-post_email.py domain_name email_address

'''

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py domain_name email_name")
        exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    var = {'email': email}
    r = requests.post(url, data=var)
    print(r.text)
