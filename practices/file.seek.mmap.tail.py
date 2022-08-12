#!/usr/bin/env python3
import mmap
import os


def tail(filename, n):
    """Returns last n lines from the filename. No exception handling"""
    size = os.path.getsize(filename)
    print(size)
    with open(filename, "rb") as f:
        # for Windows the mmap parameters are different
        fm = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
        try:
            for i in range(size - 1, -1, -1):
                if fm[i] == "\n":
                    n -= 1
                    if n == -1:
                        break
            return fm[i + 1 if i else 0 :].splitlines()
        finally:
            fm.close()


if __name__ == "__main__":
    print(tail("/tmp/data.txt", 5))
