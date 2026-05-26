'''-----------------Loops--------------------'''

#Loops are used to repeat instructions
#loop means doing something again and again automatically

# Python has two main loop types:

'''----------------for loops----------------'''
# for loop
# for loop runs once for each item in a sequence.


#Syntax


# for condition:
#     do something

#Example

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


for i in range(5):
    print("Hello")


#Loops with condition
numbers = [1, 2, 3, 4, 5]

#prints  even number
for num in numbers:
    if num % 2 == 0:
        print(num)

#prints  odd number
for num in numbers:
    if num % 2 != 0:
        print(num)


#prints square numbers
for num in numbers:
    print(num*num)

#prints cube numbers
for num in numbers:
    print(num ** 3)



'''---------------------while loops----------------'''

# A while loop repeats as long as a condition is True.
# “Keep doing this UNTIL something becomes false.”

#syntax

#  while condition:
#     do something

#Example

# count = 1

# while count < 5:
#     print(count)
#     count += 1


#Real world Login system example

# email = ""
# password = ""
# attempts = 0

# while email != "devniraj4@gmail.com" and password != "1234" and attempts < 3:
#     email = input("Enter email: ")
#     password = input("Enter a password: ")
#     attempts += 1

#     if email != "devniraj4@gmail.com" and password != "1234":
#         print("❌Wrong email and password")

# if email == "devniraj4@gmail.com" and password == "1234":
#     print("Login Successful ✅")
# else:
#     print("Account Locked 🔒")

#Practice 

#WAP to find the sum of first n numbers. (using while)




'''---------------------------Break and continue in python---------------------------'''

# break exits the loop immediately
# continue skips to the next iteration

for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)



#Practice Qs1

#print numbers from 1 to 100 

count = 1

while count < 100:
    print(count)
    count += 1


#Print numbers from 100 to 1

count = 100
while count >= 1:
    print(count)
    count -= 1


#Print the elements of a following list using a loop

numbers= [1,4,9,16,25,36,49,64,81,100]

for num in numbers:
    print(num)



#Search for a number x in this tuple using loop:

numbers= (1,4,9,16,25,36,49,64,81,100)
x = 36


for num in numbers:
    if num == x:
        print("The Number is :", x)
    




'''---------------------------------range------------------------------'''
#
#range() functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number

#syntax
#range(start, stop, step)

#print number from 1 to 100

for i in range(1,100):
    print(i)

#print number from 100 to 1

for i in range(100,0,-1):
    print(i)


#Print the multiplication of table number n

n = int(input("Enter a number: "))

for i in range(1, 21):
    print(f"{n} x {i} = {n * i}")


#Find the factorial of first n numbers (using for)

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("The Factorial of a number is: ", fact)




'''---------------------------pass Statement----------------------'''

#pass is a null statement that does nothing. It is used as a placeholder for future code.
#generally used in execption handling

#syntax

# for el in range(10):
# pass


#WAP to find the factorial of first n numbers. (using for)
