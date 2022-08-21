#!/usr/bin/env python3

def a(x):
   r = True
   for i in range(2, x):
      if (x % i) == 0:
        r = False
      return r

print(a(5))
print(a(6))
