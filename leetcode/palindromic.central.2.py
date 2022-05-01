#!/usr/bin/env python3

def longestPalindrome(s):
    if not s:
        return s
    
    answer = (0,0)
    for mid in range(len(s)):
        answer = max(answer,get_palindrome_from(s,mid,mid))
        answer = max(answer,get_palindrome_from(s,mid,mid+1))
        
    return s[answer[1]: answer[0] + answer[1]]

def get_palindrome_from(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right -left -1, left +1

if __name__ == '__main__':
    print(longestPalindrome('abcba'))