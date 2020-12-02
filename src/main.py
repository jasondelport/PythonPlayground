import os
import sys

import functions as func

print (f'version -> {sys.version}')
print (f'version info -> {sys.version_info}')
print (f'path -> {sys.path}')
print (f'cwd -> {os.getcwd()}')

for k, v in os.environ.items():
    print(f'{k} -> {v}')

print (f'arguments -> {str(sys.argv)}')

x = 3              # a whole number                   
f = 3.1415926      # a floating point number              
name = "Python"    # a string

print(x)
print(f)
print(name)

combination = name + " " + name
print(combination)

sum = f + f
print(sum)

squares = [1, 4, 9, 16, 25]
print(squares)

func.greetings()
