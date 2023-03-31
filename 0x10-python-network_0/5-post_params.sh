#!/bin/bash
#sends post request with some variables sent with it
curl -sX POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
