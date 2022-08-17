#!/usr/bin/env python3
nextval = 0


def append_next(tolist=[]):
    global nextval
    nextval += 1
    tolist.append(nextval)
    return tolist


a = append_next()
print(a)
for i in range(3):
    a = append_next(a)

b = append_next()
for i in range(3):
    a = append_next(b)

print(a)
print(b)
