#!/bin/bash
# curl get size in bytes
curl -s -X POST -H "Content-Type: application/json" --data "@$1" "$2"
