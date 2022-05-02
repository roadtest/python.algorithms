#!/usr/bin/env python3
def strStr(source, target):
    if not target:
        return 0
    for i in range(len(source)):
        if source[i: i + len(target)] == target:
            return i
    return -1
    
if __name__ == '__main__':
    print(strStr("dafabcdfabc","abc"))