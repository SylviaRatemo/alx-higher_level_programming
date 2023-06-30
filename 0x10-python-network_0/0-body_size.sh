#!/usr/bin/env bash
# curl get size in bytes
curl -so /dev/null -w '%{size_download}' "$1"
