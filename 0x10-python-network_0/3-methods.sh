#!/bin/bash
#This script shows all HTTP methods the server will accept.
curl -sl "$1" | grep "Allow" | cut -d " " -f 2-
