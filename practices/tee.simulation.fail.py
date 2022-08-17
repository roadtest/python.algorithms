#!/usr/bin/env python3

import sys
import subprocess

"""
sinks = sys.argv[1:]
print(sinks)
sinks = [open(sink, "w") for sink in sinks]
sinks.append(sys.stderr)
while True:
    input = sys.stdin.read(1024)
    if input:
        for sink in sinks:
            sink.write(input)
    else:
        break
"""

proc = subprocess.Popen(
    ["ping", "192.168.1.29"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

with open("logfile.txt", "w") as log_file:
    while proc.poll() is None:
        line = proc.stderr.readline()
        if line:
            print("err: " + line.strip())
            log_file.write(line)
        line = proc.stdout.readline()
        if line:
            print("out: " + line.strip())
            log_file.write(line)
