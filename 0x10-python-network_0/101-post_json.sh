#!/bin/bash
#sends json post request with contnets of a file and displays body of respons
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
