#!/bin/bash
#make a post request with email an subject as params
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
