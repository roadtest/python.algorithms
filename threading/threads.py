#!/usr/bin/env python
import threading
import time

# A CPU heavy calculation, just
# as an example. This can be
# anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")

def threaded(n):
    threads = []

    for i in range(n):
        t = threading.Thread(target=heavy, args=(500,i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

start = time.time()
threaded(80)
end = time.time()
print("Took: ", end - start)

# This takes about 47s on my system

# If the heavy function had a lot of
# blocking IO, like network calls or
# filesystem operations, this would 
# be a big optimization though

# The reason this is *not* an optimization
# for CPU bound functions, is the GIL!
