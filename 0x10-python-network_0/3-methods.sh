#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
