#!/bin/bash
#This script shows all HTTP methods the server will accept.
curl -sl "$1" | grep -i Allow | cut -d ' ' -f2-
