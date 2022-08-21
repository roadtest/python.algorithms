#!/usr/bin/env python3

import os

last_line = ""
inputFile = "/tmp/1.txt"
with open(inputFile, "rb") as f:
    f.seek(-2, os.SEEK_END)  # -2 because last character is likely \n
    cur_char = f.read(1)

    while cur_char != "\n":
        last_line = str(cur_char.decode()) + last_line
        print(last_line)
     #   f.seek(-2, os.SEEK_CUR)
        f.seek(-2, 1)
        cur_char = f.read(1)

    print(last_line)
