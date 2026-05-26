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


