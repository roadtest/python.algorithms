#!/usr/bin/env python3

def twoSum(numbers, target):
    setValues = set()
    for number in numbers:
        if target - number in setValues:
            return number, target - number
        setValues.add(number)
    return [-1, -1]

if __name__ == '__main__':
    print(twoSum([1,2,3,4,5], 91))
