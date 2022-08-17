#!/usr/bin/env python3
# open a file in writable mood
fi = open("output.txt", "w")

# initialize a list
initList = ["camel", "case", "stop"]

# print each words using loop
print("Printing using default print function")
for item in initList:
    print(item, file=fi)  # use file keyword

# print(file=fi)

# print each words using modified print function
print("Printing using modified print function")
for item in initList:
    print(item, end="-", file=fi)  # use file keyword

# close the file
fi.close()
