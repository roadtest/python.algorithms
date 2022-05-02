#!/usr/bin/env python3

def twoSum(numbers,target):
    if not numbers:
        return [-1,-1]

    nums =  [
            (number, index) for index, number in enumerate(numbers)
            ]
    nums.sort()

    left,right = 0, len(numbers) - 1
    while left < right: 
        if nums[left][0] + nums[right][0] > target: 
            right -= 1
        elif nums[left][0] + nums[right][0] < target: 
            left += 1
        else:
            return sorted([nums[left][1], nums[right][1]])
    return [-1,-1]

if __name__ == '__main__':
#    passList = [ 3,2,4,5,9]
    assert twoSum([2,1,3,4], 7) == [3,2], "output doesn't match"
#    print(twoSum(passList, 9))
#    print(passList)
