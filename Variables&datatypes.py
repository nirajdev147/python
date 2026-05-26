print("Hello ! I am Niraj" , "From Biratnagar, Nepal")

# variables in python
# variable is a name given to a memory location in a program.
# var = value

# Creating variables (no special keyword needed)
name = "Niraj"          # String (text) you can typically represent string in single, double, & triple quotes but commonly represented in double quotes
age = 25                # Integer (whole number)
height = 5.9            # Float (decimal number)
is_student = True       # Boolean (True/False)


print("My name is : " , name)
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))



# Key Points for identifiers
# 1. Naming Rules:

# Start with a letter or underscore: _name, name1
# Can't start with a number: ❌ 1name
# Use lowercase with underscores: my_age (recommended)
# Case-sensitive: name and Name are different


# Data Types
# text = "Hello"              # String
# number = 42                 # Integer
# decimal = 3.14              # Float
# yes_no = True               # Boolean
# my_list = [1, 2, 3]         # List
# my_dict = {"key": "value"}  # Dictionary



#Keywords in python
#Keywords are reserved words in python.



#comments in python

# using single hash

""" using multi-line comment """


# operators in python
# An Operator is an symbol that perform certain operation between operands.

# Arithmetic Operators( +,-,/,%,**)
# Relational/comparison operator(==, !=, < , >, <=, >=)
# Assignment operators(+=, -=, /=, %=, **=)
# Logical operators(AND, OR, NOT)


# Type Conversion in python
# Implicit Conversion(Automatic or type conversion)

#Example
# x = 5       # int
# y = 2.5     # float
# z = x + y   # z is 7.5 (float)

# Explicit Conversion(Manual or type casting)



# int(x): Convert to integer (truncates floats).
# float(x): Convert to float.
# str(x): Convert to string.
# bool(x): Convert to boolean (non-zero/non-empty is True).
# list(x), tuple(x), set(x): Convert to respective sequences.

#Example

# a = "123"      # str
# b = int(a)     # b is 123 (int)
# c = float(b)   # c is 123.0 (float)
# d = str(c)     # d is "123.0" (str)




"""input() function in Python reads a line of text from standard input (usually the keyboard) and returns it as a string."""


#Example

# name = input("Enter your name: ")  
# print("Hello, " + name)            

# val = input("Enter a value: ")
# print(type(val), val)

# val = int(input("Enter a value: "))
# print(type(val), val)

# val = float(input("Enter a value: "))
# print(type(val), val)


#WAP to input 2 numbers and print sum.

# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter a Second number: "))
# print("Sum is: ", num1 + num2)


#WAP to input side of a square and print its area.

# side = int(input("Enter a side of a square: "))
# print("Area of Square is :", side ** 2)

#WAP to input two floating point numbers and print their average.

# num1 = float(input("Enter a 1st float number: "))
# num2 = float(input("Enter a 2nd float number: "))
# print("The average of two floating point numbers is :", (num1 + num2) / 2)


#WAP to input 2 int numbers, a & b and print True if a is greater than b or equal to b. If not print false.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd  number: "))
print(a >= b )
