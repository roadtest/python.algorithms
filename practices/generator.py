list_comprehension = ['List Comprehension' for n in range(4)]
generator_expression = ('Generator expression' for n in range(4))

def even_integer_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
            
#for i in even_integer_generator(10):
  #  print(i)
    
name_list = ["Adam","Eve","John","Doe","Peter","Paul","Kevin"]
result = []
def gen_function(listName):
    for name in name_list:
      yield name.upper()
for i in gen_function(name_list):
    result.append(i)

result_generator_expression = ( name.upper() for name in name_list )
print("!!")
list(result_generator_expression)

def get_longest_name():
	full_names = (name.strip() for name in open("text/names.txt"))
	lengths = ((name,len(name)) for name in full_names)
	longest = max(lengths,key=lambda x:x[1])
