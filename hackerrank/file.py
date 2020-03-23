#!/usr/bin/env python
Output = open ('file2.txt', 'w')

with open('file1.txt', 'r') as Line:
#    line = Line.readline()
    for line in Line:
        NewLine = (f"curl -kv  {line}")
     #   Output.write(NewLine + '\n')
        Output.write(NewLine)
Output.close()

