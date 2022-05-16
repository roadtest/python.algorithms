def file_reader(file_path):
    for row in open(file_path, "r"):
        yield row

for row in file_reader('//tmp/1.txt'):
    print(row)

"""
with open is using generator, not like open to load file into memory
with open('path_to_a_large_file') as file:	
    for row in file:	
    # do something with each row	
    pass
"""
