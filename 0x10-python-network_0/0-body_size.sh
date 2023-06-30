#!/bin/bash
# curl get size in bytes
curl -so /dev/null -w '%{size_download}\n' "$1"
