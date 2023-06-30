#!/bin/bash
# curl get size in bytes
curl -so  /dev/null -w "%{http_code}\n" "$1"
