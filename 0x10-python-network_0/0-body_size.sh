#!/bin/bash
#This script displays the content-length from a HTTP request.
curl -sl "$1" | grep -i Content-Length | awk '{print$2}'
