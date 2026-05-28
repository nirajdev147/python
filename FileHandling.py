'''--------------------------File Handing in Python---------------------------'''


#File I/O refers to performing Input and Output operations on files, such as reading data, writing new information, updating existing content, or deleting files



#Types of Files

#In Python, files are generally categorized into two types:

#Text Files: These store data as characters. Examples include .txt, .docx, and .log files

#Binary Files: These do not store data in character format and include files like .mp4, .png, and .jpg

#Ultimately, all files are stored in memory as bits (0s and 1s), but they are categorized at a surface level for ease of use



#The Basic Lifecycle of File Operations(Opening, Reading, and Writing)

#1. Opening a File
#   You use the open() function, which requires the file name and the mode

# Syntax: f = open("filename", "mode")

#Default Mode: If no mode is specified, Python defaults to read mode ('r') and text mode ('t')


# 2. Reading from a File
# There are several ways to extract data:


# f.read(): Returns the entire content of the file as a string.
# f.read(n): Reads only the first n characters.
# f.readline(): Reads the file one line at a time.

'''

# Note on the Pointer: When you read a file, an internal "pointer" or "cursor" moves. If you read the entire file once, the pointer reaches the end, and subsequent read calls will return an empty string unless the file is reopened

'''

# f = open("demo.txt", "r")
# line1 = f.read()
# print(line1)
# f.close()


f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
f.close()




# 3. Writing and Appending

# Write Mode ('w'): This is an overwrite mode. It deletes existing content and writes new data. If the file doesn't exist, Python creates it.


# Append Mode ('a'): This adds new data to the end of the existing content without deleting it. Like write mode, it creates the file if it doesn't exist.


f = open("demo.txt", "a")
f.write("\nI am Learning Python")
f.close()





# 4. Closing a File
# It is crucial to use f.close() to ensure data integrity and prevent unauthorized access or accidental changes to an open file.





# Advanced File Modes
# Python provides combined modes for more complex operations:

# r+ (Read + Overwrite): Opens for reading and writing. The pointer is at the start, and it       overwrites existing data from the beginning without deleting the whole file first.


# w+ (Read + Write): Opens for reading and writing, but truncates (deletes) the file first.

# a+ (Read + Append): Opens for reading and writing. The pointer is at the end, so reading initially returns nothing unless the pointer is moved



# The with Syntax
# A more efficient way to handle files is using the with keyword.

# Syntax: with open("file.txt", "r") as f:

# Benefit: It automatically closes the file once the indented block of code is finished, which is a safer practice for programmers.


with open ("demo.txt", "r") as f:
    data = f.read()
    print(data)


with open("demo.txt", "w") as f:
    f.write("Fucking Thomas Shelby")



# Deleting Files
# To delete a file, you must import the os module, which contains a remove() function.

# Syntax:
# import os
# os.remove(filename)      #this permanently removes the data from the system.


with open("sample.txt", "w") as f:
    f.write("Fucking Thomas Shelby")

import os
os.remove("sample.txt")




# Practical Tips and Logic

# Searching: You can check if a word exists in a file using the in operator (e.g., if "word" in data:) or the .find() method.


# Replacing: To replace text, read the data into a string, use .replace("old", "new"), and then write the updated string back to the file.


# Parsing Numbers: If a file contains comma-separated numbers, you can use .split(",") to create a list of strings and then use type casting (int()) to convert them into integers for mathematical operations, such as checking for even numbers



#Example 01

#Create a new file "practice.txt" using python and add the some data 

with open("practice.txt", "w") as f:
    f.write("Hello! This is Niraj from Nepal")
    f.write("\nHello! This is Rahul from Nepal")
    f.write("\nHello! This is Sanjana from Nepal")
    f.write("\nHello! This is Alex from Nepal")


with open("practice.txt", "r") as f:
    old_data = f.read()
    print(old_data)


    new_data = old_data.replace("Hello", "Hi")
    print(new_data)

    with open("practice.txt", "w") as f:
        f.write(new_data)


    
#ExampleQs2

#Search for the word "This" exists in the file or not

# with open("practice.txt", "r") as f:
#     content = f.read()

# if "This" in content:
#     print("The Word Exists")
# else:
#     print("The Word doesnot Exists")



#using Function
def check_for_word():
    word = "This"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("The word Exits")
        else:
            print("The word doesn't Exists")

check_for_word()



#Example 03

#WAF to find in which line of the file does the word “learning”occur first. Print -1 if word not found.
with open("input.txt", "w") as f:
    f.write("I am Studying Q-basic")
    f.write("\nI am learning Q-basic")
    f.write("\nI am Writing Q-basic")


file = open("input.txt", "r")

line_no = 0
found = -1

for line in file:
    line_no += 1

    if "learning" in line:
        found = line_no
        break

file.close()

print(found)


#Example 04

#From a file containing numbers separated by comma, print the count of even numbers.

# Create and write into file
file = open("numbers.txt", "w")
file.write("10,15,22,7,8,31")
file.close()

# Open file for reading
file = open("numbers.txt", "r")

data = file.read()

numbers = data.split(",")

count = 0

for num in numbers:
    if int(num) % 2 == 0:
        count += 1

file.close()

print("Count of even numbers:", count)






#Practice Qs1

#Create a program: Ask user name + age and Save into file Then read file and show data


name = input("Enter user name: ")
age = input("Enter user age: ")


with open("demo.txt", "a") as f:
    f.write("\n" + name + "-" + age)

with open("demo.txt", "r") as f:
   data = f.read()
   print(data)

