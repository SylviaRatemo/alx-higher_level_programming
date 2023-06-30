#!/bin/bash
# curl get size in bytes
curl -sI -X OPTIONS "$1" | awk -F ': ' '/^Allow: / { print $2 }'
