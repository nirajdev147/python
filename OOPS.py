'''---------------------------OOPS in PYTHON-------------------------'''


#   Create a class of a "car" with their brand and model
class car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print("Car brand is", self.brand)


c1 = car("Toyota", "Corolla")
print(c1.brand)
print(c1.model)




#   Example of student system

class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def result(self):
        if self.marks >= 40:
            print(self.name,  "Pass")
        else:
            print(self.name, "Fail")

s1 = student("Niraj Dev", 75)
s2 = student("Niraj Das", 38)

s1.result()
s2.result()

        
#   Create class "BankAccount" With: name and balance and
#   Method with : deposit(amount), withdraw(amount) show_balance()


class BankAccount:     #class creation
    
    def __init__(self, name, balance):   #constructor initialization 
        self.name = name                  #Object Creation
        self.balance = balance


  
    def deposit(self, amount):              #Method to deposit money
        self.balance += amount
        print(amount, "deposited")

    def withdraw(self, amount):           #Check whether the balance is availabe to withdraw
        if amount > self.balance:
            print("Insufficient balance❌")
        else: 
            self.balance -= amount
            print(amount, "withdraw")

    def show_balance(self):                 #Method to show current account details
        print("Name: ", self.name)
        print("Balance: ", self.balance)
        
acc1 = BankAccount("Niraj Dev", 10000)   # created a object 
acc1.show_balance()


acc1.withdraw(3000)
acc1.show_balance()

acc1.deposit(5000)
acc1.show_balance()



#Another Example

# Create a class
class Person:
  def __init__(self, name, age):
     self.name = name
     self.age = age
     
  def greet(self):
    print("Hello, my name is", self.name)

#   def __hello():       
#       print("hello person!")


# Create an object
p1 = Person("John", 36)


# Call the greet method
p1.greet()
# print(p1.__hello())    #prints no attribute



#Private (like) attributes &  methods

#Conceptual implementation in python

#  Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.


#Call one method from another method using self:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()




#We can delete the age property using del keyword

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Niraj",24)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error




'''------------------------------------Inheritance-------------------------------------'''




# Inheritance means
# One class can reuse(child/derived) properties and methods of another (parent/base)class.


#Example to create a parent class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()




#Example to create a child class

class student(Person):
   pass                 #Use the pass keyword when you do not want to add any other properties or methods to the class.



#The child's __init__() function overrides the inheritance of the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()



#   super() Function

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Nikesh", "Dev")
x.printname()


#Coding Challenge

# Create a parent class Animal with an __init__ that takes name
# Add a method speak that prints the name
# Create a child class Dog that inherits from Animal
# Create an object d1 = Dog("Rex")
# Call d1.speak()



class Animal:  #created parent animal class 
   def __init__(self, name):
      self.name = name

   def speak(self):   #Created Method
      print(self.name)

class Dog(Animal):     #Created child class that inherited from parent class
   pass
      
d1 = Dog("Rex")       #Created object 
d1.speak()            #called object method


#Method Overriding

#Child can replace parent method

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

c1 = Child()
c1.show()


#Example of Student System

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self,name,marks):
       super().__init__(name)
       self.marks = marks

    def result(self):
       if self.marks >= 40:
          print(self.name, "Pass")
       else:
          print(self.name, "Fail")

s1 = Student("Niraj", 45)

s1.info()
s1.result()

#Create a  Parent class: Animal with method: sound() and Child class: Dog then override sound() → print "Bark"

class Animal:
   def sound(self):
      print("Animal makes sound")

class Dog(Animal):
   def sound(self):
      print("Bark")

d1 = Dog()
d1.sound()

#Types of Inheritance:

# Single Inheritance: A single child class inherits from a single parent class.


#---------------------------------------------------------------------------#
# Multi-level Inheritance: A chain of inheritance where a class inherits from a derived class.

#Example of Multi-level inheritance

class Car:
   @staticmethod
   def start():
      print("Car Started...")

   @staticmethod
   def stop():
      print("Car Stopped...")

class ToyotaCar(Car):
   def __init__(self, brand):
      self.brand = brand

class Fortuner(ToyotaCar):
   def __init__(self, type):
      self.type =type 

car1 = Fortuner("Diesel")
car1.start()



#--------------------------------------------------------------------------------------------#

# Multiple Inheritance: A single child class inherits properties from two or more independent parent classes


#----------------------------------------------------------------------------------------------#


#The super() Method: This is a special method used to access the parent class's methods, most commonly used to call the parent's constructor within the child class

class Animal:
   def sound(self):
      print("Animal makes sound")

class Dog(Animal):
   def sound(self):
    super().sound()
    print("Bark")

d1 = Dog()
d1.sound()
 

#----------------------------------------------------------------------------------------------#


# Specialized Methods and Decorators

# Class Methods: 
# Defined using the @classmethod decorator, these methods are bound to the class rather than a      specific object.
# They take cls as the first argument and are used to modify class-level state that remains consistent across all instances.


# Property Decorator: 
# The @property decorator allows a method to be accessed like an attribute
# It is particularly useful for values that need to be recalculated automatically based on other changing attributes, such as a student's percentage updating whenever their marks are modified.




















'''----------------------------------------Polymorphism---------------------------------------'''


#The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

#Example of polymorphism

class cat:
   def sound(self):
      print("Meow")

class dog:
   def sound(self):
      print("Bark")

c1 = cat()
c2 = dog()

c1.sound()
c2.sound()


#Polymorphism with Loop


class cat:
   def sound(self):
      print("Meow")

class dog:
   def sound(self):
      print("Bark")

animals = [cat(), dog()]

for animal in animals:
   animal.sound()


# 🧪 Your Practice 🔥

# Create: Class Shape with method: area() and create a Class Circle then override area → print circle area
# Then create a Class Square then override area → print square area

# Parent class
class Shape:
    def area(self):
        print("Area of shape")

# Child class
class Circle(Shape):
    def area(self):
        radius = 5
        print("Circle Area =", 3.14 * radius * radius)

# Child class
class Square(Shape):
    def area(self):
        side = 4
        print("Square Area =", side * side)


c1 = Circle()
s1 = Square()

c1.area()
s1.area()
   

      












# Operator Overloading: This is a form of polymorphism where built-in operators (like + or -) are given custom meanings for user-defined classes.

# Dunder Methods: These are special methods (double underscore methods) that Python calls internally to perform operations. 

# For example:

# __add__ for the + operator

# __sub__ for the - operator

# __gt__ for the greater-than > operator




'''------------------------------------Encapsulation-------------------------------------'''
'''------------------------------------Abstraction-------------------------------------'''



