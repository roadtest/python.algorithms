#!/usr/bin/env python3
	
# Opening "GfG.txt" text file
# in binary mode
f = open("data.txt", "rb")

# sets Reference point to tenth
# position to the left from end
f.seek(-10, 2)

# prints current position
print(f.tell())

# Converting binary to string and
# printing
print(f.readline().decode('utf-8'))

f.close()
