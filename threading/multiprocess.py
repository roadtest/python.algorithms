#!/usr/bin/env python
import time
import multiprocessing

# A CPU heavy calculation, just
# as an example. This can be
# anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")

def multiproc(n):
    processes = []

    for i in range(n):
        p = multiprocessing.Process(target=heavy, args=(500,i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

start = time.time()
multiproc(80)
end = time.time()
print("Took: ", end - start)

# This takes about 23 seconds.
# That's half of the threaded version.
# My pc has two cores, so it's exactly
# what we would expect.

# On my Mackbook Pro, with 4 cores
# that are faster as well,
# it takes 10 seconds!
