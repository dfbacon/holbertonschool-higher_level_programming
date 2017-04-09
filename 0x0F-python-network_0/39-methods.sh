#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -SI $1 | grep "Accept:" | cut -d ':' -f2
