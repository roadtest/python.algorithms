#!/usr/bin/env python3
class solution
    def longestPalindrome(self,s):
        if not s:
            return ""
        
        start, longest = 0, 0
        for middle in range(len(s)):
            #odd number of letter
            left, right = middle, middle
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if longest < right - left -1:
                longest = right - left - 1
                start = left + 1
                
            #evev number of letter
            left, right = middle, middle + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if longest < right - left - 1:
                longest = right - left - 1
                start = left + 1
            return s[start:start + longest]