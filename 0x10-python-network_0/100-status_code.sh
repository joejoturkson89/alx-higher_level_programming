#!/bin/bash
# This script sends a GET request and SHOW the response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
