#!/usr/bin/env bash
# take URL, send request, display size of body

if [$# -eq 0]; then
	echo "Usage: $0 [Insert URL]"
	exit 1
fi

url=$1
response=$(curl -sI "http://$url")
content_length=$(echo "$response" | awk '/Content-Length/ { print $2 }')

if [ -z "$content_length" ]; then
	echo "Error: Length not found"
	exit 1
fi

echo "$content_length"
