#!/bin/bash
#sends get request, displays the body and sedns a header variable
curl -s -H 'X-School-User-Id: 98' "$1"
