#!/usr/bin/env python3
import functools 
 
 
l1 = [10, 20, 30, 40, 50] 
l2 = [10, 20, 30, 50, 40, 70] 
l3 = [10, 20, 40, 30, 50] 
 
if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,l1,l2), True): 
    print ("The lists l1 and l2 are the same") 
else: 
    print ("The lists l1 and l2 are not the same") 
 
if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,l1,l3), True): 
    print ("The lists l1 and l3 are the same") 
else: 
    print ("The lists l1 and l3 are not the same") 

"""
l1 = [10, 20, 30, 40, 50] 
l3 = [50, 75, 30, 20, 40, 69] 
 
res = [x for x in l1 + l3 if x not in l1 or x not in l3]
 
print(res)
if not res:
    print("Lists l1 and l3 are equal")
else:
    print("Lists l1 and l3 are not equal")
"""
