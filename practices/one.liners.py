#!/usr/bin/env python3

from functools import reduce

result = [i**2 for i in range(10)]
# print(result)

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
print(list1[0::4])
# below is wrong
# print( [ x  x = list1(i) for i in range(0,len(list1) + 1, 4) ] )
# below is right with list comprehension
print([list1[i] for i in range(0, len(list1) + 1, 4)])
# below is using filter
print(list(filter(lambda x: x % 4 == 0, range(len(list1)))))
print([list2[index] for index in filter(lambda x: x % 4 == 0, range(len(list2)))])
# use list comprehension with if
result = [i**2 for i in range(10) if i % 2 == 0]
print(f"list with if check - {result}")

# below is enumerate
print(list(item for i, item in enumerate(list1) if i % 4 == 0))
# below is using range, is wrong
# print(list1(range(0, len(list1) + 1, 4)))
# use map to transfer list into different value
list3_iterator = map(lambda x: x**2, list1)
print(list(list3_iterator))
list4_cap = map(lambda x: x.capitalize(), list2)
print(list(list4_cap))
# use reduce
def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)
# you can use lambda instead of def function

total = reduce(lambda a, b: a + b, scores)
print(f"output of lambda with reduce - {total}")
