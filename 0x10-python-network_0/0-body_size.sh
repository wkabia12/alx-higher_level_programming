#!/bin/bash
#returns size of body content (content-length)
curl -s -I "$1" | grep Content-Length | cut -d" " -f2
