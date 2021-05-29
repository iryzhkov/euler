#!/usr/bin/env bash
cp $1 script.py
cp $2 input.txt
python3 script.py < input.txt
rm script.py input.txt