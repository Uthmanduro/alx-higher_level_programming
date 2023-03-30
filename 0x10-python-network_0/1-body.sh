#!/bin/bash
#takes in a url and sends a get request then displays the body of the response
curl -L -s "$1"
