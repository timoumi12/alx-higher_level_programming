#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -H "X-School-User-Id: 98" -sX GET $1 -L
