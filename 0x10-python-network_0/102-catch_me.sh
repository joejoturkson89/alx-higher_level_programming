#!/bin/bash
# This script SENDs a request to 0.0.0.0:5000/catch_me with the message "You get me!".
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
