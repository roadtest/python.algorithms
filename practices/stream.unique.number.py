#!/usr/bin/env python3

def firstUniqueNumber(nums, number):
    if not nums: 
        return -1;

    counter = {}

    for num in nums:
        counter[num] = counter.get(num,0) + 1
        if num == number:
            break
    else:
        return -1

    for num in nums:
        if counter[num] == 1:
            return num

"""
        if num == number: 
            break
    return -1
"""

if __name__ == '__main__':
    assert firstUniqueNumber([1,2,3,1,3,4,5], 5) == 2, "wrong"
    assert firstUniqueNumber([1,2,3,1,2,4,5], 5) == 3, "wrong"
