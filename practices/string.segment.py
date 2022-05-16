#!/usr/bin/env python3

def can_segment_string(s, dictionary):
  for i in range(1, len(s) + 1):
    first = s[0:i]
    print(first)
    if first in dictionary:
      second = s[i:]
      if not second or second in dictionary or can_segment_string(second, dictionary):
        return True
  return False

def stringSeg(s, dictionary):
    if dictionary.count(s):
        return True
    for element in dictionary: 
        s = s.replace(element,'')
        if not s:
            return True
    return False

if __name__ == '__main__':

    assert stringSeg("testing", ["test", "abc", "ing"]) == True
    assert stringSeg("testing", ["test", "abc", "inkg"]) == False
    assert can_segment_string("hellonow",['hell', 'hello', 'now', 'on']) == True

#If it is set, you need to use in to check whether it has string or not
#string is substring check using in, find and index
