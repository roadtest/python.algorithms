#!/usr/bin/env python3
def find_sum_of_two(A,val):
    scannedInteger = set()
    for element in A:
        if val - element in scannedInteger: 
            return True
        scannedInteger.add(element)
    return False;


if __name__ == '__main__':

    assert find_sum_of_two([1,2,3], 5) == True, "should exist"
    assert find_sum_of_two([1,2,3], 6) == False, "should not exist"


