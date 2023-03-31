#!/bin/bash
#makes a request that cause server to respod with You got me! in the body
curl -sv 0.0.0.0:5000/catch_me | grep "You got me!"
