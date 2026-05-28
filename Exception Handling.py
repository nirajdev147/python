'''---------------------------Exception Handling (try-except)---------------'''


# This helps programs:
# Handle errors without crashing

#  Common Errors

# Error	Meaning

# ValueError ----> wrong value

# ZeroDivisionError	-----> divide by zero

# FileNotFoundError	 --> missing file

# IndexError	----> invalid index

#---------------------------------------------------------------------------------#

#ValueError

# try:
#     num = int(input("Enter number: "))
#     print(num)

# except:
#     print("Invalid input")


#---------------------------------------------------------------------------------#


#ZeroDivisionError

# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))

#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")


#---------------------------------------------------------------------------------#

#FileNotFoundError

# try:
#     f = open("data.txt", "r")
#     print(f.read())

# except FileNotFoundError:
#     print("File not found")







# Create:
# 👉 calculator with exception handling

# Handle:

# invalid input
# divide by zero

# 🔥 This is real beginner project practice.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

except ValueError:
    print("Invalid input ❌ Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero ❌")

else:
    print("Calculation successful ✅")
