#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    sum=0
    print(Counter(ar))
    for values in Counter(ar).values():
        sum+=values//2
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

