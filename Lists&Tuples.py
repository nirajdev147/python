'''-------------------------List---------------------------'''
#list is an Ordered collection, in which you can change(mutable), add, remove elements.
#It is created with square brackets: []
#A built-in data type that stores set of values.
#It can store elements of different types (integer, float, string, etc.)

#syntax
#list: my_list = [1, 2, 3]


#Example

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[1] = "blueberry"
print(fruits)


numbers = [1, 2, 3]
numbers.append(4)
numbers.insert(0, 0)
numbers.remove(2)
numbers.pop()
print(numbers)  


# List Slicing
# similar to string slicing

#syntax
# list_name[ starting_idx : ending_idx ]




'''----------------List Methods-------------------'''

#Various types of list methods are given below:

# list.append()         #adds one element at the end

# list.insert( idx, el ) #insert element at index

# list.sort( ) #sorts in ascending order

# list.reverse( ) #reverses list

# list.sort( reverse=True ) #sorts in descending order

# list.remove(1) #removes first occurrence of element

# list.pop( idx ) #removes element at idx





'''------------------------Tuple------------------------------'''
#Tuple is an Ordered collection, in which you cannot change elements(immutable) after creation.
#It is Created with parentheses: ()
#It is usually a bit faster and uses less memory.

#syntax
#tuple: my_tuple = (1,2,3)

#Example

colors = ("red", "green", "blue")
#colors[1] = "yellow"  # ❌ change not allowed
print(colors)


point = (10, 20)
x, y = point
print(x, y)  # 10 20





#Conversion between list and tuples

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)


#list can contain tuples and vice-versa

data = [(1, 2), (3, 4)]
print(data)
settings = ("high", [1, 2, 3])
print(settings)



#tuple methods

#tup.index(el) #returns index of first occurrence

#tup.count(el)   #counts total occurrences




'''------------------------------Practice-----------------------'''


#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# m1 = input("Enter your 1st fav movie name: ")
# m2 = input("Enter your 2nd fav movie name: ")
# m3 = input("Enter your 3rd fav movie name: ")
# movie_list = [m1,m2,m3]
# print(movie_list)


#WAP to count the number of students with the "A" grade in the following tuple.

# ["C" ,"D","A","A","B","B","A"]

# Store the above values in a list & sort them from "A" to "D"    

# list = ["C", "D", "A", "A", "B", "B", "A"]
# list.sort()
# print(list)


# tup = ("C", "D", "A", "A", "B", "B", "A")
# count_A = tup.count("A")
# print("Number of A's:", count_A)
# print("Tuple:", tup)





#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

def is_palindrome(lst):
    # Create a copy and reverse it
    reversed_list = lst.copy()
    reversed_list.reverse()
    # Check if original and reversed are the same
    return lst == reversed_list

# Test cases
list1 = [1, 2, 3, 2, 1]
print(f"Is {list1} a palindrome? {is_palindrome(list1)}")  # True

list2 = [1, "abc", "abc", 1]
print(f"Is {list2} a palindrome? {is_palindrome(list2)}")  # True

list3 = [1, 2, 3, 4, 5]
print(f"Is {list3} a palindrome? {is_palindrome(list3)}")  # False