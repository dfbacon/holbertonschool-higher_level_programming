#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -HsLXT "Content-Type: application/json" POST "$2" "$1"
