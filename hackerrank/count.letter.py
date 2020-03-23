#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
#word = 'CatBatSatFatOr'
# Splitting at 3 
#print([word[i:i+3] for i in range(0, len(word), 3)]) 
# or in python3, split(string) or list(string)

def repeatedString(s, n):
    if len(s) == 1:
        return n

    elif len(s) < n : 
        NewString = list(s*(math.ceil((n-len(s))/len(s)) + 1))
        print(NewString)
    else:
        NewString = list(s)
    Num = NewString[0:n].count('a')
    return Num
#can be replaced by return s.count('a') *( n//(len(s))) + s[:(n%(len(s)))].count('a')
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
