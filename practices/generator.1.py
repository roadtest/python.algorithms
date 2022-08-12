#!/usr/bin/env python3

import sys

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sys.getsizeof(x))
print(sys.getsizeof(range(1, 11)))

x = range(1, 11)
print(type(x))
print(type(iter(x)))
print(list(iter(x)))


def squareNumbers(numberList):
    for num in numberList:
        print(f"{num} squared is {num ** 2}")
        yield (num * num)

myNumbers = squareNumbers([1, 23, 3, 4, 4, 4, 4, 5])
print(myNumbers)

for num in myNumbers:
    print(num)
