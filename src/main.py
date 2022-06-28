
import os
import platform
import sys

import functions as func
import get_logging as log
import http_client as http
from rectangle import Rectangle

print (f'version -> {sys.version}')
print (f'version info -> {sys.version_info}')
print (f'path -> {sys.path}')
print (f'cwd -> {os.getcwd()}')
print (f'arguments -> {str(sys.argv)}')
print ('Python', platform.python_version())
print('__name__: ', __name__)

# this python 2 code breaks in python -> print "Hello, Python!"
print ("Hello, Python!")

name = "jason"
print(f'Hello {name}!')

# environment variables
#for k, v in os.environ.items():
#    print(f'{k} -> {v}')

# arguments passed in at the command line, seperated by spaces


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

# multi lline comment
"""
In Python, the pass keyword is an entire statement in itself. 
This statement doesn’t do anything: it’s discarded during the 
byte-compile phase. But for a statement that does nothing, 
the Python pass statement is surprisingly useful.
"""

func.greetings()

func.json_examples()

func.lists()

func.files()

func.errors()

func.dicts()


rectangle = Rectangle(5,4)
rectangle.do_area();
# dynamic function calls
rectangle.solve_for('area')


def area(length: int, width: int):
    print(length * width)

# dynamic function calls
area_func = globals()["area"]

area_func(5, 5)

http.doConnect()

log.doLogging()
