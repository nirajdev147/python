'''------------------------------Dictionary----------------------------'''
#Dictionaries are used to store data values in key:value pairs
#They are unordered, mutable(changeable) & don’t allow duplicate keys

#Example

student = {
    "name": "Alice",
    "age": 21,
    "major": "Math",
    "marks":{
        "chem": 85,      #Nested dictionaries
        "sci":48
    }
}

print(student["name"])    # Alice
print(student.get("age")) # 21
print(student.get("major")) #Math
print(student["marks"]["sci"])   #48
print(student.pop("age"))
print(student)




#Common operations to be performed on dictionary

# Add/update: student["grade"] = "A"

student = {
    "name": "Niraj",
    "age": 25,
    "major": "Math"
}
print(student)
student["grade"] ="A"
print(student)    



# Remove: student.pop("age")

student = {
    "name": "Sunny",
    "age": 18,
    "major": "Science"
}
print(student.pop("age"))
print(student)



# Check key: "name" in student

student = {
    "name": "Rebecca",
    "age": 29,
    "major": "Computer Science"
}

for key, value in student.items():
    print(key, value)



# Dictionary Methods

# myDict.keys( ) #returns all keys
# myDict.value() #returns all values
# myDict.items( ) #returns all (key, val) pairs as tuples
# myDict.get( "key"" ) #return the key according to value

# myDict.update( newDict ) #inserts the specified items to the dictionary





'''------------------------------------Set-----------------------------'''

# Set is the collection of the unordered items.
# No Duplicates
# Each element in the set must be unique & immutable.

#Example

fruits = {"apple", "banana", "orange"}
fruits.add("kiwi")
fruits.add("apple")  # already exists, so no duplicate

print("banana" in fruits)  # True
print(fruits)



#Common Operations performed in Set

# Add: fruits.add("grape")

fruits = {"apple", "banana", "orange"}
print(fruits.add("grape"))
print(fruits)

# Remove: fruits.remove("orange")
fruits = {"apple", "banana", "orange", "grape"}
print(fruits.remove("orange"))
print(fruits)



# Set operations examples
a = {"apple", "banana", "cherry"}
b = {"banana", "cherry", "date"}

print("Set a:", a)
print("Set b:", b)

# Union: all unique elements from both sets
union_result = a | b
print("Union (a | b):", union_result)

# Intersection: elements common to both sets
intersection_result = a & b
print("Intersection (a & b):", intersection_result)

# Difference: elements in a but not in b
difference_result = a - b
print("Difference (a - b):", difference_result)



'''-----------------------------------------Practice-----------------------------------------'''


# Store following word meanings in a python dictionary :
''' 
table : "a piece of furniture", "list of facts & figures",
cat : "a small animal"

'''

my_dict = {
    "table" : [ "a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"    
}
print(my_dict)



#Example02

'''
You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.

"python","java","C++","python","javascript","java","python","java","C++","C"

'''

student = {
    "subjects" : ["python","java","C++","python","javascript","java","python","java","C++","C"]
}

unique_subjects = set(student["subjects"])
print("No of unique_subjects:", len(unique_subjects))



#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start withan empty dictionary & add one by one. Use subject name as key & marks as value.


marks = {}

first = int(input("Enter the marks of first subject:"))
marks.update({"Sci" : first})

second = int(input("Enter the marks of second subject:"))
marks.update({"Math" : second})

third = int(input("Enter the marks of third subject:"))
marks.update({"Comp sci" : third})

print(marks)