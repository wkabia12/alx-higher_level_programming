#!/bin/bash
#make a get request with custom header equal to 98
curl -s -H "X-School-User-Id: 98" "$1"
