#!/usr/bin/env python3

def validPalindrome(s):
    if s is None:
        return False

    left,right = findDifference(s, 0, len(s) -1)
    if left >= right; 
        return True

    return isPalindrome(s,left + 1, right) or isPalindrome(left, right -1)

def isPalindrome(s, left, right):
    left, right = findDifference(s, left, right)
    return left >= right

def findDifference(s, left, right):
    while left < right: 
        if s[left] != s[right]: 
            return left, right
        left += 1
        right -= 1
    return left, right 


if __name__ = '__main__':
    validPalindrome('abcba')
