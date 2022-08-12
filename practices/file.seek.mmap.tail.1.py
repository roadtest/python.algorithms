#!/usr/bin/env python3
import io  # Gets consistent version of open for both Py2.7 and Py3.x
import itertools
import mmap


def skip_back_lines(mm, numlines, startidx):
    """Factored out to simplify handling of n and offset"""
    for _ in itertools.repeat(None, numlines):
        startidx = mm.rfind(b"\n", 0, startidx)
        if startidx < 0:
            break
    return startidx


def tail(f, n, offset=0):
    # Reopen file in binary mode
    with io.open(f.name, "rb") as binf, mmap.mmap(
        binf.fileno(), 0, access=mmap.ACCESS_READ
    ) as mm:
        # len(mm) - 1 handles files ending w/newline by getting the prior line
        startofline = skip_back_lines(mm, offset, len(mm) - 1)
        if startofline < 0:
            return []  # Offset lines consumed whole file, nothing to return
            # If using a generator function (yield-ing, see below),
            # this should be a plain return, no empty list

        endoflines = startofline + 1  # Slice end to omit offset lines

        # Find start of lines to capture (add 1 to move from newline to beginning of following line)
        startofline = skip_back_lines(mm, n, startofline) + 1

        # Passing True to splitlines makes it return the list of lines without
        # removing the trailing newline (if any), so list mimics f.readlines()
        return mm[startofline:endoflines].splitlines(True)
        # If Windows style \r\n newlines need to be normalized to \n, and input
        # is ASCII compatible, can normalize newlines with:
        # return mm[startofline:endoflines].replace(os.linesep.encode('ascii'), b'\n').splitlines(True)


utf8stdout = open(1, "w", encoding="utf-8", closefd=False)  # fd 1 is stdout
with open("/tmp/data.txt", "rb") as fd:
    output = tail(fd, 5)
    print(output.encode("unicode_escape"))
