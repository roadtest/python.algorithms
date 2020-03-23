#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
#    total=0
#    print(Counter(ar))
#    for value in ar:
#        sum[value]+=1

#    sum = dict((i, ar.count(i)) for i in ar)
#    for key,value in sum.items():
#       total+=value//2
#       # print(f"{key} {value}")
#    total = [i**2 for i in ar]
    total = dict()
    for i in ar: 
        total[i] = total.get(i,0) + 1
       # total[i] = total[i] + 1

    return total

if __name__ == '__main__':

    n = 10

   # ar = [10, 20, 10, 30, 10, 10, 10, 20, 40, 50, 50]
    ar = ['a', 'b', 'c']

    result = sockMerchant(n, ar)

    print(result)
