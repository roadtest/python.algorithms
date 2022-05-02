#!/usr/bin/env python3
from pipe import dedup, where, select, sort

num_list_with_duplicates = [1, 4, 2, 27,
                            6, 8, 10, 7, 13, 19, 21, 20, 7, 18, 27]
# perform pipe oerations
results = list(num_list_with_duplicates 
                | dedup 
                | where(lambda x: x % 2 == 1)
                | select(lambda x: x**2)
                | sort
            )

print(results)
