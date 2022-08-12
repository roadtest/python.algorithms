#!/usr/bin/env python3
import timeit
import shutil
import os

f = open('f1', 'wb')
f.write(os.urandom(8 * 1024 * 1024))

p1 = "f1"
p2 = "f2" 

shutil.copyfile(p1, p2)
