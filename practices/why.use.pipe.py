#!/usr/bin/env python3
num_list_with_duplicates = [1, 4, 2, 27,
                            6, 8, 10, 7, 13, 19, 21, 20, 7, 18, 27]

# Remove duplicates from the list
num_list = list(dict.fromkeys(num_list_with_duplicates))

# Filter for odd numbers
odd_list = [num for num in num_list if num % 2 == 1]

# Square the numbers
odd_square = list(map(lambda x: x**2, odd_list))

# Sort values in ascending order
odd_square.sort()

print(odd_square)
