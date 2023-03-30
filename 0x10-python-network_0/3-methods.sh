#!/usr/bin/bash
#takes in a utl and displays all http methods the server will accept
curl -s -I "$1" | awk '/Allow/ {print substr($0, index($0, $2))}'
