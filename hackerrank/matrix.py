#!/usr/bin/env python
# -*- coding: utf-8 -*-

#arr = []
#for _ in range(6):
#    arr.append(list(map(int, input().rstrip().split())))
#arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]

'''
max = 0 
for row in range(4):
    for col in range(4):
        sum = 0 
        for element in range(3):
        #    print(arr[row][col+element], arr[row+2][col+element])
            sum = sum + arr[row][col+element] + arr[row+2][col+element]
        sum = sum + arr[row+1][col+1]
        if row == 0 and col == 0:
            max = sum
        elif sum > max:
            max = sum
print(max)
'''

print(max([sum(arr[i-1][j-1:j+2] + [arr[i][j]] + arr[i+1][j-1:j+2]) for j in range(1, 5) for i in range(1, 5)]))

