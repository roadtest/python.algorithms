#!/usr/bin/env python3

from collections import deque

inputFile = "/tmp/1.txt"

def stream_docs(filename):
    count = 0
    with open(filename, 'r') as fd:
        for line in fd:
            count += 1
            yield line


#for line in stream_docs(inputFile):
#    print(line)
for i in range(0,len(deque(stream_docs(inputFile),maxlen=5))):
    print(deque(stream_docs(inputFile),maxlen=5)[i])

