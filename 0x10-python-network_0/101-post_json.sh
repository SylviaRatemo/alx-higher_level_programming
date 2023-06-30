#!/bin/bash
# curl get size in bytes
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
