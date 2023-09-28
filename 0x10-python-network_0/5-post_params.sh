#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -d "email: test@gmail.com&subject: I will always be here for PLD" -sX POST $1 -L
