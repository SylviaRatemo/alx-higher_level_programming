#!/bin/bash
# curl get size in bytes
echo "POST params:\n"
curl -sS -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
