#!/usr/bin/env python3
import math

def f(a,x): 
  if not a or not x :
      return -1;
  answer = -1;
  low = 0;
  high = len(a) - 1;
  while low <= high:
    mid = low + math.floor(( high - low) / 2);
    if (a[mid] == x): 
      return x 
    elif (a[mid] < x) : 
      answer = a[mid];
      low = mid + 1;
    else:
      high = mid - 1; 
  return answer;


if __name__ == '__main__':
    a = [ 3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21 ];
    try: 
        assert f(a,12) == 12   , "number found"
        assert f(a,13) == 12   ,  "smaller number found"
        assert f(a, 2) == -1   ,  "out of bounds too small"
        assert f(a, 22) == 21  ,  "out of bounds too large"
        assert f(a, 3) == 3    ,  "exact left boundary"
        assert f(a, 21) == 21  ,  "exact right boundary"
        assert f([], x) == -1  ,  "empty array"
        assert f(null, x) == -1  , "invalid input"
    #except NameError as e:
    except Exception as e:
        print("error message is " + str(e))