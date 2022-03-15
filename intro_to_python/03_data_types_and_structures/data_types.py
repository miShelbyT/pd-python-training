import sys

name = 'Shelby'

# # string = f'Hi my name is: {name}'
# does not work here because my Python isn't new enough. Need 3.6

# # alternatively, 
string = "hi my name is: {}".format(name)

print(string)

name = 'World'
program = 'Python'
# print(f'Hello {name}! This is {program}')

print(name + program)

print(sys.version_info)