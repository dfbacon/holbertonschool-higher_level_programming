#!/usr/bin/python3
'''

This is the '9-starwars' module.

9-starwars takes in a string and sends a search request to the Star Wars API
(https://swapi.co/documentation).

Assignment Requirements:
* Use the Star Wars API search endpoint (https://swapi.co/documentation#search)
* Use the string argument as the search value of the request
* The body response must be JSON and converted to a Python dictionary.
* Display: Number of result: <count>
* Display the name of each result (see example below)
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don't need to check arguments passed to the script (number or type)
* You don't need to manage the pagination

Usage:
$ ./9-starwars.py string

'''

if __name__ == "__main__":
