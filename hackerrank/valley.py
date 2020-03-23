#!/usr/bin/env python
# -*- coding: utf-8 -*-

String = "UUDDUDDDUUDDDDUDUUUUUDDDDUUU"
VALLEY = PRE = SUM = 0
for Letter in String:
#    PRE = SUM
#    if Letter == 'U':
#        SUM += 1
#    else:
#        SUM -= 1
# you can save without using PRE
#    if PRE < 0 and SUM == 0:
#    if Letter == 'U' and SUM == 0:
#        VALLEY += 1
    if Letter == 'D':
        SUM -= 1
    else:
        SUM += 1
        if SUM == 0:
            VALLEY += 1

print(f"number of valley is {VALLEY}")


