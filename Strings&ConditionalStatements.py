#Strings
#Strings is a datatype that converts a sequence of characters(text).

#Basic Operations of Strings


#concatenation
# "hello" + "world" "helloworld"


# length of str
# len(str)->3
#len("Hello")->5

#Common Strings Methods
# .upper() - converts to uppercase
# .lower() - converts to lowercase;
# .strip() - removes whitespace
# .split() - splits string into list
# .replace(old, new) - replaces characters
# .count("am") -counts the occurrence of substr in string
# .endsWith("er.") -returns true if string ends with substr

# str = "spider man"
# print(str.upper())
# print(str.lower())
# print(str.endswith("o"))
# print(str.replace("spider man", "hello"))
# print(str.find("h"))
# print(str.count("h"))
# print(str.split())




#Slicing
# Slicing means accessing the parts of a string

# str[ starting_idx : ending_idx ] #ending idx is not included

# str = "ApnaCollege"

# str[ 1 : 4 ] is "pna"

# str[ : 4 ] is same as str[ 0 : 4] and its output is "Apna"

# str[ 1 : ] is same as str[ 1 : len(str) ] and its output is "Apna College"




# Negative Index

# str = "Apple"

# str[ -3 : -1 ] is "pl"




#  A  p  p  l  e
# -5 -4 -3 -2 -1

# Output-> pl



"""Practice"""

# WAP to input user’s first name & print its length.

# user = input("Enter user first name: ")
# print(len(user))



#WAP to find the occurrence of ‘$’ in a String.

# user = input("Enter a string : ")
# print(user.count("$"))



# Conditional Statements
# Conditional statements allow you to execute code based on certain conditions.

"""
if (condition1):
    Statement1      # runs if condition1 is True
elif (condition2):
    Statement2      # runs if condition2 is True
else:
    StatementN      # runs if all conditions are False
   
"""


#Practice

# WAP to check if a number entered by the user is odd or even.

# num = int(input("Enter a number: "))

# if (num % 2 == 0):
#     print("even")
# else:
#     print("odd")



# WAP to find the greatest of 3 numbers entered by the user.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))


# if(a>b and a>c):
#     print("the greatest number is : ", a)
# elif(b>c):
#     print("the greatest number is : ", b)
# else:
#     print("the greatest number is : ", c)






# WAP to check if a number is a multiple of 7 or not.

# num = int(input("Enter a number:"))

# if(num % 7  == 0 ):
#     print("number is multiple of 7")
# else:
#     print("number is not multiple of 7")