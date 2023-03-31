#!/bin/bash
#displays the status code of the response
curl -s -w %{http_code} "$1" -o /dev/null
