#!/usr/bin/env python3

# Scan the file system for ownerless files

import os
import os.path

# Build a set of the UIDs present in /etc/passwd

uidset = set()

for line in open("/etc/passwd"):
    split = line.split(":")
    if "#" in split[0]:
        continue
    uidset.add(int(split[2]))

## Alternative implementation
## for user in pwd.getpwall():
##     uidset.add(user.pw_uid)

# Walk the specified directory
testdir = "/tmp/1"

for folder, dirs, files in os.walk(testdir):
    for file in files:
        # Build the full pathname of the file
        path = folder + "/" + file
        ##        if os.path.islink(path):
        ##            print(path + " is a symlink ... skipping")
        ##            continue
        try:
            attributes = os.stat(path)
        except FileNotFoundError:
            # This will occur if we encounter a broken symlink
            print(path + " not found")
            continue

        if attributes.st_uid not in uidset:
            print(path + " has no owner")
