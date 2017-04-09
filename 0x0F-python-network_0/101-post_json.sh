#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -H "Content-Type: application/json" -sLXT POST "$2" "$1"
