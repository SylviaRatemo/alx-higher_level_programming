#!/bin/bash
# curl get size in bytes
curl -s -o /dev/null -w "%{http_code}\n" "$1"
