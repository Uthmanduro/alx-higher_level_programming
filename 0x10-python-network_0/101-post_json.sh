#!/bin/bash
#sends json post request with contnets of a file and displays body of respons
curl -sv -X POST -H "Content-Type: application/json" -d "$2" "$1"
