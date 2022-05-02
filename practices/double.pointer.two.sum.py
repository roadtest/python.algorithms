#!/usr/bin/env python3

def twoSum(numbers,target):
    numbers.sort()

    left,right = 0, len(numbers) - 1
    while left < right: 
        if numbers[left] + numbers[right] > target: 
            right -= 1
        elif numbers[left] + numbers[right] < target: 
            left += 1
        else:
            return numbers[left], numbers[right]
    return [-1,-1]

if __name__ == '__main__':
    passList = [ 3,2,4,5,9]
    print(twoSum(passList, 10))
    print(passList)
