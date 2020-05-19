#!/usr/bin/env python
#from lib import heavy
import time

# A CPU heavy calculation, just
# as an example. This can be
# anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")

def sequential(n):
    for i in range(n):    
        heavy(500, i)

start = time.time()
sequential(80)
end = time.time()
print("Took: ", end - start)

# On my system, this takes
# about 46 seconds.
