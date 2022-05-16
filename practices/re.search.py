#!/usr/bin/env python3
from re import search
fullstring = "abcdefgd"
substring = "d"

if search(substring, fullstring):
	print("found")
else:
	print("no")
