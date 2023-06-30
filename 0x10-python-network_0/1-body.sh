#!/bin/bash
# curl get size in bytes
response=$(curl -Ls "$1")
echo "$response"
