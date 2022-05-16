#!/usr/bin/env python3
full_names = (name.strip() for name in open("/tmp/1.txt"))
lengths = ((name,len(name)) for name in full_names)
#if you enable below line, iterator will be consumed
#print(list(lengths))
longest = max(lengths,key=lambda x:x[1])
print(longest)
