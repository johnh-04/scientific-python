# Introduction to Python Programming


'''
python3 --version (check Python version)
python3 file.py (run a Python file)

pip3 install library_name (install a library)
pip3 install library_name==version (install a specific version of a library)
pip3 --upgrade library_name (upgrade a library to the latest version)
pip3 uninstall library_name (uninstall a library)

pip3 show library_name (show information about the library)
pip3 list (list installed libraries)

pip3 freeze > requirements.txt (save installed libraries to a file)
pip3 install -r requirements.txt (install libraries from a file)
'''


# Hello World in Python
print("Hello, World!")


# Variables and Data Types
name = "Alice"
age = 30
height = 5.5
is_student = True

print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(height))  # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>


# Multiple Assignment / Same Value Assignment
a, b, c = 1, 2.5, "Test"
print(a, b, c)  # Output: 1 2.5 Test

x = y = z = 10
print(x, y, z)  # Output: 10 10 10


# Conditional Statements (and, or, not)
num = 10
if num > 0 and num < 20:
    print("Positive and less than 20")
elif num < 0 or num > 20:
    print("Negative or greater than 20")
else:
    print("Zero")

if not num == 0:
    print("Not zero")


# Loops
x = 0
while x < 5:
    print(x)
    x += 1

for i in range(5):
    print(i)


# String: ordered, mutable, allows duplicates, heterogeneous
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!


# List: ordered, mutable, allows duplicates, heterogeneous
mixed_list = [1, "two", 3.0, True]
print(mixed_list)  # Output: [1, 'two', 3.0, True]

print(mixed_list[0])  # Output: 1
print(mixed_list[1])  # Output: two
print(mixed_list[2])  # Output: 3.0
print(mixed_list[3])  # Output: True

print(mixed_list[-1])  # Output: True (last element)

print(mixed_list[1:3])  # Output: ['two', 3.0] (slicing)
print(mixed_list[:2])  # Output: [1, 'two'] (slicing)
print(mixed_list[2:])  # Output: [3.0, True] (slicing)

print(mixed_list[::2])  # Output: [1, 3.0] (every second element)
print(mixed_list[::-1])  # Output: [True, 3.0, 'two', 1] (reversed)

print(mixed_list + [5, "six"])  # Output: [1, 'two', 3.0, True, 5, 'six'] (concatenation)

print(len(mixed_list))  # Output: 4 (length of the list)

print("two" in mixed_list)  # Output: True (membership test)
print("three" not in mixed_list)  # Output: True (membership test)

for item in mixed_list:
    print(item)  # Output: Iterating through the list

mixed_list[1] = "changed"
print(mixed_list)  # Output: [1, 'changed', 3.0, True] (modified list)

mixed_list.append("new")
print(mixed_list)  # Output: [1, 'changed', 3.0, True, 'new'] (appended element)

mixed_list.insert(2, "inserted")
print(mixed_list)  # Output: [1, 'changed', 'inserted', 3.0, True, 'new'] (inserted element)

mixed_list.extend([7, "eight"])
print(mixed_list)  # Output: [1, 'changed', 'inserted', 3.0, True, 'new', 7, 'eight'] (extended list)

mixed_list.remove("changed")
print(mixed_list)  # Output: [1, 'inserted', 3.0, True, 'new', 7, 'eight'] (removed element)

last_element = mixed_list.pop()
print(last_element)  # Output: 'eight' (popped element)
print(mixed_list)  # Output: [1, 'inserted', 3.0, True, 'new', 7] (list after popping)

del mixed_list[0]
print(mixed_list)  # Output: ['inserted', 3.0, True, 'new', 7] (deleted first element)

mixed_list.clear()
print(mixed_list)  # Output: [] (cleared list)

nums = [5, 2, 9, 1]
nums.sort()
print(nums)  # Output: [1, 2, 5, 9] (sorted list)
nums.sort(reverse=True)
print(nums)  # Output: [9, 5, 2, 1] (sorted in reverse)

if 2 in nums:
    print("2 is in the list")  # Output: 2 is in the list

if 10 not in nums:
    print("10 is not in the list")  # Output: 10 is not in the list


# Set: unordered, mutable, no duplicates, heterogeneous
num_set = {1, 2, 2, 3, 4, 5}
print(num_set)  # Output: {1, 2, 3, 4, 5} (duplicates removed)

print(len(num_set))  # Output: 5 (number of unique elements)

for item in num_set:
    print(item)  # Output: Iterating through the set

num_set.add(6)
print(num_set)  # Output: {1, 2, 3, 4, 5, 6} (added element)

num_set.remove(3)
print(num_set)  # Output: {1, 2, 4, 5, 6} (removed element)

num_set.discard(10)  # No error if element not found
print(num_set)  # Output: {1, 2, 4, 5, 6} (discarded element)

A = {1, 2, 3}
B = {3, 4, 5}

print(3 in A)  # Output: True (membership test)
print(10 not in A)  # Output: True (membership test)

print(A | B)  # Output: {1, 2, 3, 4, 5} (union)
print(A.union(B))  # Output: {1, 2, 3, 4, 5} (union)

print(A & B)  # Output: {3} (intersection)
print(A.intersection(B))  # Output: {3} (intersection)

print(A - B)  # Output: {1, 2} (difference)
print(A.difference(B))  # Output: {1, 2} (difference)

print(A ^ B)  # Output: {1, 2, 4, 5} (symmetric difference)
print(A.symmetric_difference(B))  # Output: {1, 2, 4, 5} (symmetric difference)


# Dictionary: unordered, mutable, unique keys, heterogeneous values
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# person = dict(name="Alice", age=30, city="New York")  # Alternative way to create a dictionary
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

print(person["name"])  # Output: Alice
print(person["age"])  # Output: 30
print(person["city"])  # Output: New York

print(person.get("age"))  # Output: 30
print(person.get("country", "Unknown"))  # Output: Unknown (default value)

print(len(person))  # Output: 3 (number of key-value pairs)

print("name" in person)  # Output: True (membership test)
print("city" not in person)  # Output: False (membership test)

for key in person:
    print(key)  # Output: Iterating through keys

for value in person.values():
    print(value)  # Output: Iterating through values

for key, value in person.items():
    print(f"{key}: {value}")  # Output: Iterating through key-value pairs

print(person.keys())  # Output: dict_keys(['name', 'age', 'city']) (keys view)
print(person.values())  # Output: dict_values(['Alice', 30, 'New York']) (values view)
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')]) (items view)

person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'} (updated value)

person["country"] = "USA"
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'} (added key-value pair)

del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'} (deleted key-value pair)

person.pop("age")
print(person)  # Output: {'name': 'Alice', 'country': 'USA'} (popped key-value pair)

person.popitem()
print(person)  # Output: {'name': 'Alice'} (popped last key-value pair)

person.clear()
print(person)  # Output: {} (cleared dictionary)

students = {
    "Alice": {"age": 30, "grade": "A"},
    "Bob": {"age": 25, "grade": "B"}
}
print(students)  # Output: {'Alice': {'age': 30, 'grade': 'A'}, 'Bob': {'age': 25, 'grade': 'B'}} (nested dictionary)

print(students["Alice"]["grade"])  # Output: A (accessing nested dictionary)
print(students["Bob"]["age"])  # Output: 25 (accessing nested dictionary)


# Tuple: ordered, immutable, allows duplicates, heterogeneous
point = (1, 2)
print(point)  # Output: (1, 2)

print(point[0])  # Output: 1
print(point[1])  # Output: 2


# Functions
def sum(a, b):
    return a + b
print(sum(3, 5))  # Output: 8

def greet(name="World"): # Default parameter value
    return f"Hello, {name}!"
print(greet())  # Output: Hello, World!
print(greet("Alice"))  # Output: Hello, Alice!

x = 10  # Global variable
def modify_global():
    global x  # Declare x as global to modify it
    y = 5  # Local variable
    x += y  # Modify global variable x
modify_global()
print(x)  # Output: 15 (modified global variable)

def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function()  # Calling the inner function
print(outer_function())  # Output: Hello from the inner function! (output of the outer function)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120 (factorial of 5)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))  # Output: 55 (10th Fibonacci number)