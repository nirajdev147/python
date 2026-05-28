'''------------------What is a Module--------------------?'''

#   A Module is simply a python file containing code.
#   Python already has many built-in modules.


#   Common Math Functions

# | Function           | Meaning     |
# | ------------------ | ----------- |
# | `math.sqrt()`      | square root |
# | `math.factorial()` | factorial   |
# | `math.pi`          | π value     |
# | `math.ceil()`      | round up    |
# | `math.floor()`     | round down  |



#Generate math functions

import math

print(math.sqrt(25))  
print(math.factorial(8))
print(math.pi)


#Generate random number
import random
print(random.randint(1,100))



#enerate random names from choice

import random

names = ["Dev", "Alex", "Ram"]

print(random.choice(names))




#Generate time
import time

print(time.time())




#   Create Your Own Module 

import my_module
my_module.greet("Niraj Dev")


#   Import Specific Function

from math import sqrt
print(sqrt(49))