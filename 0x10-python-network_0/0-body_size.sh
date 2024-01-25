#!/bin/bash
#This script displays the content-length from a HTTP request.
curl -sl "$1" | grep "Content-Length:" | cut -d " " -f 2 
