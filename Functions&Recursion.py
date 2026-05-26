''''----------------------Functions'-----------------------'''


#A function is a reusable block of code, instead of writing same code again and again, we create a function


#Syntax

# def function_name(parameters):
#     # code
#     return result


#Example

def greet():              #parameter
    print("Hello Dev")

greet()                  #argument




def add(x,y):
    return x * y

result = add(3,5)
print(result)


#Example 01: Even or Odd

def check(num):
    if num%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

check(6)


#Example 02: Find maximum number

def max(a,b):

    if a > b:
        return a
    
    else:
        return b

print(max(4,6))




#Example 03: Multiplication table

def mul_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

mul_table(19)


#Example:04 Create a function of cube(n)

def cube(n):
    return n ** 3

print(cube(4))


#Example:05  Create a function of average(a, b, c)

def average(a,b,c):
    return (a + b + c) / 3

print(average(1,2,3))



#Example06: WAF to convert USD to NPR.


def convert(usd):
    return usd * 154.46

usd = float(input("Enter a usd:"))

npr = convert(usd)
print(f"NPR = {npr:.2f}")










'''---------------------------Recursion-------------------------------------'''

#Recursion means a function calling itself


#Recursion with countdown
def countdown(n):

    if n == 0:  #until the condition is true then it returns and stop the recursion
        return 
    
    print(n)     #prints 6
    countdown(n-1) #calls countdown 5

countdown(6)




#Recursion with factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(0))  # 120



#Example01: Print numbers from 1 to 5:


def num(n):
    if n == 6:
        return 
    print(n)
    num(n+1)

num(1)


#Example02: Print numbers from 5 to 1:

def num(n):
    if n == 0:
        return
    print(n)
    num(n-1)

num(5)

#Example 03: Print fibonacci series

def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(6))


#Example 04: Print numbers in ascending order

def num(n):
    if n == 0:
        return
    
    num(n-1)
    print(n)

num(6)


#Example 05: Print numbers in descending order

def num(n):
    if n == 0:
        return
    
    print(n)
    num(n-1)
    
num(6)


#Example06: Create recursion to calcualte  1² + 2² + 3² + ... + n²

def func(n):
    if n == 0:
        return 0
    
    return n*n + func(n-1)

print(func(4))



#Example 07: Write a recursive function to print all elements in a list.
#Hint : use list & index as parameters.

def print_list(lst, index):
    
    if index == len(lst):
        return

    print(lst[index])
    print_list(lst, index + 1)


numbers = [1, 2, 3, 4, 5]
z
print_list(numbers, 0)