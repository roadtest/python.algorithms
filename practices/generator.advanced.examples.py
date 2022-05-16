#!/usr/bin/env python3
def custom_chain(*iterables):	
    for iterable in iterables:	
        print("inside" + str(iterable))
        yield from iterable	


for x in custom_chain([1, 2, 3], 'abc'):	
    print(x, end=' ')
