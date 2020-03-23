#!/usr/bin/env python
import sys
#n = int(input().strip())
#a = [int(c_temp) for c_temp in input().strip().split(' ')]
n = 20
a = [0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0]
NumJump = -1
i = 0
while i < n:
    if i < n-2 and a[i+2] == 0:
        i += 1
    NumJump += 1
    i += 1
print(NumJump)
