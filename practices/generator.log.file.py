"""
def file_reader(file_path):
    for row in open(file_path, "r"):
        yield row
#when you open, you need close file afterwards
for row in file_reader("//tmp/1.txt"):
    print(row)
"""


def file_reader(file_path):
    # with open is using generator, not like open to load file into memory
    with open(file_path) as file:
        for row in file:
            # do something with each row
            yield row


for i in file_reader("//tmp/1.txt"):
    print(i.strip())
