#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -H "email: test@gmail.com" -H "subject: I will always be here for PLD" -sX POST $1 -L
