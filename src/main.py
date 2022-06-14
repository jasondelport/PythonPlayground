import json
import os
import platform
import sys
from contextlib import suppress

import functions as func

print (f'version -> {sys.version}')
print (f'version info -> {sys.version_info}')
print (f'path -> {sys.path}')
print (f'cwd -> {os.getcwd()}')

print ('Python', platform.python_version())

# this python 2 code breaks in python -> print "Hello, Python!"
print ("Hello, Python!")

name = "jason"
print(f'Hello {name}!')

#for k, v in os.environ.items():
#    print(f'{k} -> {v}')

#print (f'arguments -> {str(sys.argv)}')

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

for i in range(5):
    print(i)
    i += 2

some_letters = ['a', 'b', 'c', 'd', 'e']
for letter in some_letters:
    # do something
    pass

for i, letter in enumerate(some_letters, start=0):
    print(f'item at index {i} is {letter}')

#OLD WAY
f = open('test.txt')  # note default is mode='r'
print(f.read())
f.close()

#NEW WAY
with open('test.txt') as f: # no close() needed
   print(f.read())

# handling errors
try:
    raise RuntimeWarning('Something could go wrong')
except RuntimeWarning as e:  # as e is optional
    print(e)

empty_dict = {}  # or dict()
my_dict = {'key': 'value'}
# How to get value from dict
try:
    my_dict['a']  # raises KeyError if 'a' not in dictionary
except:
    print('error')

print(my_dict.get('a', 'bob'))

if 'key' in my_dict:
    val = my_dict['key']
val = my_dict.get('key', None)
if val is not None: pass
with suppress(KeyError):
    val = my_dict['key']
print(val)

# multi lline comment
"""
In Python, the pass keyword is an entire statement in itself. 
This statement doesn’t do anything: it’s discarded during the 
byte-compile phase. But for a statement that does nothing, 
the Python pass statement is surprisingly useful.
"""

# handling json files
f = open('test.json',)
data = json.load(f) # parse JSON from URL or file
print(data)
print(data['attribute'])
print(data['object'])
print(data['object']['attribute0'])
print(data['list'])
print(data['list'][0]['attribute1'])
f.close()

json_str = """{
    "attribute": "value"
}
"""
data_loads = json.loads(json_str) # parse JSON from a string
print(data_loads)
