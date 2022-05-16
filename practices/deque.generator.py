#!/usr/bin/env python3
from collections import deque
import sys

list1 = [ 2,4,11,3,4,5,6,56,6,666,12, 0,3,44,4930,33,343,4343]
minElement = deque([max(list1[0],list1[1]),min(list1[0],list1[1])],maxlen=2)
maxElement = deque([min(list1[0],list1[1]),max(list1[0],list1[1])],maxlen=2)

# deque([1, 2, 3, 4, 5], maxlen=5)
#d.append(10)
#sys.getsizeof()
stream_list1=(x for x in list1)
print(type(stream_list1))
print(sys.getsizeof(stream_list1))
print(sys.getsizeof(list1))
print("==")

small=list1[0]
big=list1[0]

for element in stream_list1: 
    if element > big:
        big = element
        maxElement.append(big)
    if element < big and element > maxElement[0]:
        maxElement[0] = element
    if element > small and element < minElement[0]:
        minElement[0] = element
    if element < small:
        small = element
        minElement.append(small)

print(minElement,maxElement)
