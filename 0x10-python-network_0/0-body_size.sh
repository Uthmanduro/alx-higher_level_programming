#!/usr/bin/bash
#takes in a url, sends a request to the url and displays the size of the body
curl -i -s "$1" | awk '/Content-Length/ {print $2}'
