#!/usr/bin/env python3

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
    if x == 4:
        break 
else:
    print ("else block in loop")
print ("Out of loop")

