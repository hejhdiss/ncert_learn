s='''
Here are some common Python programming examples and codes relevant for NCERT Class 12. These include examples for basic syntax, conditionals, loops, functions, string manipulation, lists, dictionaries, file handling, and more.

1. Basic Input and Output

# Taking input from the user and printing it
name = input("Enter your name: ")
print("Hello, " + name)
2. Arithmetic Operations

a = 5
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
3. Conditional Statements (if-elif-else)

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
4. Loops
For Loop

# Printing numbers from 1 to 5
for i in range(1, 6):
    print(i)
While Loop

# Printing numbers from 1 to 5 using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1
5. Functions

# Function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial of 5:", factorial(5))
6. String Manipulation

text = "Hello, World!"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace 'World' with 'Python':", text.replace("World", "Python"))
print("Find index of 'o':", text.find("o"))
7. Lists

# Creating a list and performing operations
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
numbers.append(60)          # Adding an element
print("After append:", numbers)
numbers.remove(30)          # Removing an element
print("After remove:", numbers)
print("Length of list:", len(numbers))  # Length of list
print("Sorted list:", sorted(numbers))  # Sorting the list
8. Dictionaries

# Creating a dictionary and accessing elements
student = {
    "name": "Alice",
    "age": 17,
    "marks": 95
}
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Marks:", student.get("marks"))
student["age"] = 18  # Modifying a value
print("Updated Age:", student["age"])
9. File Handling
Writing to a File

with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file.")
Reading from a File

with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)
10. Simple Programs
Check if a Number is Prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
Check if a Number is an Armstrong Number

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == num
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
11. Bubble Sort Algorithm

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted List:", sorted_numbers)
12. Counting Occurrences of Each Character in a String

def count_characters(text):
    count_dict = {}
    for char in text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict
text = "hello world"
print("Character Count:", count_characters(text))
These examples cover fundamental programming concepts typically required in the Class 12 curriculum, including conditionals, loops, functions, lists, dictionaries, file handling, and some commonly used algorithms. Let me know if you’d like more details on any specific program or topic!'''
def studyexamples():

    """
    Retrieve common Python programming examples for NCERT Class 12.

    This function returns the content of the global variable 's', which contains
    a collection of Python programming examples and codes relevant for Class 12
    students. These examples cover basic syntax, conditionals, loops, functions,
    string manipulation, lists, dictionaries, file handling, and more.
    """

    global s
    return s
k='''
For NCERT Class 12 students in India, Python programming focuses on fundamental concepts and includes many standard functions. Below is a categorized list of common Python functions and methods relevant to the Class 12 syllabus. This list includes standard library functions, mathematical operations, and string manipulation, which are typically covered at this level.

1. Basic Built-in Functions
These are core Python functions that students often use:

print() - Displays output to the console.
input() - Accepts user input.
len() - Returns the length of an iterable (e.g., string, list).
type() - Returns the type of an object.
int(), float(), str() - Type conversion functions.
round() - Rounds a floating-point number to the nearest integer.
abs() - Returns the absolute value of a number.
min() / max() - Returns the minimum or maximum of an iterable.
sum() - Sums up elements in an iterable.
sorted() - Returns a sorted list from an iterable.
range() - Generates a sequence of numbers.
enumerate() - Provides a counter with an iterable.
zip() - Combines multiple iterables element-wise.
reversed() - Reverses the order of an iterable.
2. Mathematical Functions (Requires import math)
The math module provides additional functions for mathematical calculations:

math.sqrt() - Returns the square root of a number.
math.pow() - Raises a number to a power.
math.ceil() / math.floor() - Rounds up or down to the nearest integer.
math.factorial() - Returns the factorial of an integer.
math.gcd() - Computes the greatest common divisor.
math.sin(), math.cos(), math.tan() - Trigonometric functions.
math.log() - Returns the natural logarithm of a number.
math.pi - Constant representing the value of π.
3. String Functions and Methods
Strings in Python have many useful methods for manipulation:

str.upper() / str.lower() - Converts to uppercase or lowercase.
str.capitalize() - Capitalizes the first character.
str.find() - Finds the first occurrence of a substring.
str.replace() - Replaces substrings within a string.
str.split() - Splits a string by a delimiter.
str.join() - Joins elements of an iterable with a string separator.
str.strip() - Removes leading and trailing whitespace.
str.startswith() / str.endswith() - Checks if a string starts or ends with a specific substring.
str.isalpha(), str.isdigit(), str.isalnum() - Checks if the string has alphabetic, numeric, or alphanumeric characters.
4. List Functions and Methods
Lists, a common data structure, have a variety of methods:

list.append() - Adds an element to the end of the list.
list.extend() - Adds multiple elements to the end.
list.insert() - Inserts an element at a specified index.
list.pop() - Removes and returns an element at an index.
list.remove() - Removes the first occurrence of a specified value.
list.sort() / sorted() - Sorts elements in ascending or descending order.
list.reverse() - Reverses the list in place.
list.index() - Returns the index of the first occurrence of a specified value.
list.count() - Counts occurrences of a specified value.
5. Dictionary Functions and Methods
Dictionaries are also commonly used and have unique methods:

dict.keys() - Returns all keys in the dictionary.
dict.values() - Returns all values.
dict.items() - Returns all key-value pairs as tuples.
dict.get() - Returns the value for a specified key.
dict.update() - Updates the dictionary with another dictionary’s key-value pairs.
dict.pop() - Removes and returns a value by key.
6. Additional Functions
Some additional Python functions that may be introduced:

all() - Returns True if all elements in an iterable are True.
any() - Returns True if any element in an iterable is True.
map() - Applies a function to all items in an iterable.
filter() - Filters items in an iterable based on a function.
lambda functions - Anonymous functions often used with map() and filter().
7. File Handling Functions
Basic functions to handle file operations:

open() - Opens a file.
file.read() - Reads data from a file.
file.write() - Writes data to a file.
file.readline() / file.readlines() - Reads lines from a file.
file.close() - Closes the file.
These functions cover most of what’s included in the NCERT Class 12 curriculum for Python programming. Let me know if you’d like more information on any specific function!'''
def studyfunctions():

    """
    Retrieve detailed study material.

    This function returns the content of the global variable 'k', which contains
    a categorized list of common Python functions and methods relevant to the
    Class 12 syllabus. It includes standard library functions, mathematical
    operations, string manipulation, list and dictionary methods, and file
    handling functions.
    """

    global k
    return k
m='''
Here’s a brief explanation of each topic in Python for Class 12 students, broken down by each major concept as per the NCERT syllabus. You can use this as a guide or as study material for students.

1. Basic Operations
Input and Output: In Python, input() is used to take input from the user, and print() is used to display output. For example:


name = input("Enter your name: ")
print(f"Hello, {name}")
Arithmetic Operations: Python allows basic arithmetic operations like addition (+), subtraction (-), multiplication (*), division (/), modulus (%), and exponentiation (**).


a = 5
b = 3
print(a + b)  # Output: 8
2. Conditional Statements (if, elif, else)
Conditionals: Conditional statements help us make decisions in a program. The if statement runs a block of code if the condition is True, elif is used for additional checks, and else runs if all conditions are False.

Example:


x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
3. Loops (for, while)
For Loop: Used to iterate over a sequence (like a list, string, or range). It repeats a block of code a fixed number of times.


for i in range(5):  # Will print numbers 0 to 4
    print(i)
While Loop: Executes a block of code as long as the given condition is True.


i = 0
while i < 5:
    print(i)
    i += 1
4. Functions
Functions: Functions are blocks of reusable code that perform specific tasks. You define a function with the def keyword, and it can take inputs (parameters) and return outputs.

Example:


def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # Output: Hello, Alice
Functions help in breaking down complex problems into smaller, manageable tasks.

5. String Manipulation
Strings: Strings are sequences of characters. You can perform various operations like concatenation, slicing, and case conversion.


text = "Hello World"
print(text.upper())  # Output: "HELLO WORLD"
print(text[0:5])     # Output: "Hello"
String Methods:

upper(): Converts to uppercase.
lower(): Converts to lowercase.
replace(): Replaces a substring.
Example:


greeting = "Hello"
greeting = greeting.replace("e", "a")  # Output: "Hallo"
6. Lists
Lists: Lists are ordered collections that can store multiple items of different types. You can add, remove, and access elements in a list.

Example:


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add to the end
fruits.remove("banana")  # Remove item
print(fruits)  # Output: ['apple', 'cherry', 'orange']
7. Dictionaries
Dictionaries: A dictionary is a collection of key-value pairs. Each key is unique and is used to access the corresponding value.

Example:


student = {"name": "John", "age": 18, "marks": 90}
print(student["name"])  # Output: John
student["age"] = 19  # Update value
8. File Handling
File Handling: Python can read from and write to files using the open() function. You can open a file in different modes (r for read, w for write, etc.).

Example:


# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, World!
9. Algorithms (Prime, Armstrong, etc.)
Prime Numbers: A prime number is a number that is greater than 1 and only divisible by 1 and itself.

Example of checking if a number is prime:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
Armstrong Numbers: An Armstrong number is a number where the sum of its digits raised to the power of the number of digits is equal to the number itself.

Example:


def is_armstrong(num):
    digits = [int(digit) for digit in str(num)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == num
10. SQL (Structured Query Language)
SQL is used to interact with relational databases. It allows you to insert, update, delete, and query data in a database.

Database Connection: To interact with databases in Python, the sqlite3 module is commonly used. Here’s an example of how to connect and run SQL queries.

import sqlite3

# Connecting to SQLite database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Creating a table
cursor.execute(\'\'\'CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)\'\'\')

# Inserting data
cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 18)")

# Querying data
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())  # Fetches all rows

conn.commit()
conn.close()
11. Stack (LIFO - Last In, First Out)
A stack is a linear data structure where elements are added or removed from the same end. It follows the LIFO principle: the last element added is the first one to be removed.

Example of implementing a stack:


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Pushes an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pops an item from the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def peek(self):
        """Returns the top element without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
12. Queue (FIFO - First In, First Out)
A queue is a linear data structure where elements are added at the rear and removed from the front. It follows the FIFO principle: the first element added is the first one to be removed.

Example of implementing a queue:


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Adds an item to the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Removes an item from the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.queue) == 0

    def front(self):
        """Returns the front element without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"
13. CSV (Comma-Separated Values)
CSV is a file format used to store tabular data. Python provides the csv module to read from and write to CSV files.

Example of reading and writing CSV files:


import csv

# Writing to a CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Country'])
    writer.writerow(['Alice', 18, 'USA'])
    writer.writerow(['Bob', 20, 'UK'])

# Reading from a CSV file
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
14. Binary Files
Binary files are files that contain data in binary format (0s and 1s). You can read and write binary files using Python's built-in open() function with the 'b' mode.

Example of reading and writing binary files:


# Writing to a binary file
with open('example.bin', 'wb') as file:
    data = b'\\x00\\x01\\x02\\x03\\x04'
    file.write(data)

# Reading from a binary file
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)  # Output: b'\\x00\\x01\\x02\\x03\\x04'
15. Exceptions and Error Handling
Exceptions are runtime errors that occur in Python. You can handle these errors using try, except, else, and finally blocks to prevent the program from crashing.

Example of error handling:


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input types"
    else:
        return result
    finally:
        print("Execution complete.")

print(divide(10, 0))  # Output: Error: Division by zero
Common Python Errors:

ZeroDivisionError: Raised when dividing by zero.
TypeError: Raised when an operation is applied to an object of inappropriate type.
IndexError: Raised when an invalid index is accessed in a list.
ValueError: Raised when a function receives an argument of the correct type but inappropriate value.
16. Recursion
Recursion is when a function calls itself to solve smaller instances of the same problem. It is important to define a base case to avoid infinite recursion.

Example of calculating factorial using recursion:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
17. Sets
Sets are unordered collections of unique elements. They are useful for performing operations like union, intersection, and difference.

Example of set operations:


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set1 & set2)  # Output: {3, 4}

# Difference
print(set1 - set2)  # Output: {1, 2}
18. Tuples
Tuples are similar to lists, but they are immutable. Once created, you cannot modify their values.

Example of tuple operations:


tuple1 = (1, 2, 3, 4)
print(tuple1[0])  # Output: 1
19. Lambda Functions
Lambda functions are small anonymous functions defined with the lambda keyword. They are typically used for short, throwaway functions.

Example of a lambda function:


square = lambda x: x * x
print(square(5))  # Output: 25
20. List Comprehensions
List Comprehensions provide a concise way to create lists. It allows you to transform one list into another by applying an expression.

Example of list comprehension:


numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # Output: [1, 4, 9, 16, 25]
Conclusion
With these additional topics, Class 12 students will have a broad understanding of Python and related concepts. By learning these, students will be equipped to handle a wide variety of problems, from database operations with SQL to advanced data structures like stacks, queues, and recursion.
These topics will also provide a strong foundation for future studies in computer science, data science, and software development.'''
def studyshort():

    """
    Retrieve short study notes.

    This function returns the content of the global variable 'm', which contains
    brief explanations and examples on Python topics intended for Class 12 students.
    These notes cover basic operations, conditionals, loops, functions, and more,
    providing a concise overview of essential Python concepts.
    """

    global m
    return m
z='''
To work with MySQL databases in Python, you can use the mysql-connector-python library. This allows you to interact with MySQL databases, execute queries, and handle data. Here's how you can install and use MySQL Connector for Python.

1. Installation
First, you need to install the mysql-connector-python package. You can install it using pip:

bash
Copy code
pip install mysql-connector-python
2. Connecting to a MySQL Database
To connect to a MySQL database, you need the hostname, username, password, and database name.

Here’s how to connect to the MySQL database:


import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",       # MySQL server hostname or IP
    user="your_username",   # MySQL username
    password="your_password",  # MySQL password
    database="your_database"   # Database name
)

# Creating a cursor object
cursor = conn.cursor()

# Checking the connection
if conn.is_connected():
    print("Successfully connected to MySQL database!")

# Don't forget to close the connection
conn.close()
3. Creating a Database and Table
Once connected, you can create a database and a table for storing your data.

Example to create a database and a table:


# Establish connection
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)

cursor = conn.cursor()

# Creating a database
cursor.execute("CREATE DATABASE IF NOT EXISTS studentDB")

# Selecting the database
conn.database = 'studentDB'

# Creating a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(10)
)
""")
print("Database and Table Created Successfully!")

conn.close()
4. Inserting Data into a Table
You can insert data into your MySQL database using the INSERT INTO SQL statement.

Example to insert data into the students table:


# Connecting to the database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="studentDB"
)

cursor = conn.cursor()

# Inserting data into the students table
cursor.execute("""
INSERT INTO students (name, age, grade)
VALUES (%s, %s, %s)
""", ("Alice", 18, "A"))

# Commit the transaction
conn.commit()

print("Data inserted successfully!")

# Close the connection
conn.close()
5. Retrieving Data from a Table
To retrieve data, you use the SELECT SQL statement.

Example to fetch all records from the students table:


# Connecting to the database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="studentDB"
)

cursor = conn.cursor()

# Fetching data from the students table
cursor.execute("SELECT * FROM students")

# Fetching all results
result = cursor.fetchall()

for row in result:
    print(row)

# Close the connection
conn.close()
6. Updating Data in a Table
To update existing data, you can use the UPDATE SQL statement.

Example to update the grade of a student:


# Connecting to the database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="studentDB"
)

cursor = conn.cursor()

# Updating data in the students table
cursor.execute("""
UPDATE students
SET grade = %s
WHERE name = %s
""", ("B", "Alice"))

# Commit the transaction
conn.commit()

print("Data updated successfully!")

# Close the connection
conn.close()
7. Deleting Data from a Table
To delete data, you can use the DELETE SQL statement.

Example to delete a student record:


# Connecting to the database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="studentDB"
)

cursor = conn.cursor()

# Deleting data from the students table
cursor.execute("DELETE FROM students WHERE name = %s", ("Alice",))

# Commit the transaction
conn.commit()

print("Data deleted successfully!")

# Close the connection
conn.close()
8. Handling Exceptions
When working with databases, it's important to handle exceptions that may occur during database operations.

Example of exception handling in MySQL queries:

python
Copy code
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="studentDB"
    )

    cursor = conn.cursor()

    # Example query that could raise an exception
    cursor.execute("SELECT * FROM non_existing_table")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        conn.close()
9. Closing the Connection
Remember to always close the connection after you're done with your database operations to free up resources.


if conn.is_connected():
    conn.close()
    print("Connection closed")
Conclusion
This brief overview shows how to connect to a MySQL database using mysql-connector-python, perform CRUD (Create, Read, Update, Delete) operations, and handle basic errors. This will be helpful for Class 12 students to integrate database operations into their Python programs.

You can combine these operations with other topics, such as SQL queries, data analysis, and user interaction, to build a complete project or solve real-world problems using Python.'''
def studymysqlpython():

    """
    Retrieve MySQL study notes for Python.

    This function accesses the global variable 'z', which contains comprehensive
    notes and examples on using MySQL with Python. These notes include instructions
    on how to connect to a database, perform CRUD operations, and handle exceptions.
    
    Returns
    -------
    str
        The content of the global variable 'z', providing a detailed guide for 
        Class 12 students on integrating MySQL database operations into Python programs.
    """

    global z
    return z
a='''
1. Python Basics
Data Types
Python supports several built-in data types:

int: Integer numbers (e.g., 5, -10)
float: Decimal numbers (e.g., 3.14, -0.001)
str: Strings of characters (e.g., "hello", 'Python')
bool: Boolean values (True, False)
list: A collection of ordered elements (e.g., [1, 2, 3])
tuple: An immutable collection (e.g., (1, 2, 3))
dict: A collection of key-value pairs (e.g., {"name": "John", "age": 18})
set: A collection of unique unordered elements (e.g., {1, 2, 3})
NoneType: A special type representing None (used for null values)
Variables and Constants
Variables hold data of any data type and can be reassigned.
Constants are typically written in uppercase letters, but Python does not have a built-in constant data type.
2. Control Flow
Conditional Statements
if: Executes a block of code if the condition is True.
elif: Checks additional conditions if the if condition is False.
else: Executes when all the previous conditions are False.
Example:


x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
Loops
for loop: Used to iterate over a sequence (like lists, ranges).
while loop: Repeats a block of code as long as the condition is True.
Example:


# For loop example
for i in range(1, 6):  # From 1 to 5
    print(i)

# While loop example
x = 0
while x < 5:
    print(x)
    x += 1
Break and Continue
break: Exits the loop prematurely.
continue: Skips the current iteration and moves to the next one.
3. Functions
Defining Functions
Functions help you organize your code into smaller, reusable parts. Functions are defined using the def keyword.

Example:


def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
Arguments and Return Values
You can pass parameters to functions and return values using the return keyword.
default arguments: You can set default values for parameters.
variable-length arguments: Use *args and **kwargs for a variable number of arguments.
Example with default argument:


def greet(name="Student"):
    return f"Hello, {name}!"

print(greet())          # Output: Hello, Student!
print(greet("Alice"))   # Output: Hello, Alice!
4. Data Structures
Lists
Lists are mutable, ordered collections that can store mixed data types.
Operations on lists:

Append: Adds an item to the end.
Remove: Removes an item by value.
Pop: Removes an item by index and returns it.
Example:


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adds "orange" to the list
fruits.remove("banana")  # Removes "banana"
print(fruits)  # Output: ['apple', 'cherry', 'orange']
Tuples
Tuples are similar to lists but are immutable (cannot be changed after creation).
Example:


colors = ("red", "green", "blue")
# colors[0] = "yellow"  # This will raise an error since tuples are immutable
Dictionaries
Dictionaries store key-value pairs. Keys are unique, and values can be of any data type.
Example:


student = {"name": "John", "age": 18, "marks": 90}
print(student["name"])  # Output: John
student["age"] = 19  # Update age
Sets
Sets are unordered collections with unique elements.
Example:


unique_numbers = {1, 2, 3, 3}
print(unique_numbers)  # Output: {1, 2, 3}
5. File Handling
Python provides built-in methods to work with files, allowing you to read from and write to files.

Reading from a File

with open("file.txt", "r") as file:
    content = file.read()
    print(content)
Writing to a File

with open("file.txt", "w") as file:
    file.write("Hello, world!")
Handling CSV Files
Use the csv module to read and write CSV files.


import csv

# Writing to CSV
with open("data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["Alice", 18, "USA"])

# Reading from CSV
with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
6. MySQL with Python
Connecting to MySQL Database

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="yourdatabase"
)

cursor = conn.cursor()
Executing SQL Queries
Example of creating a table:


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    grade VARCHAR(10)
)
""")
CRUD Operations in MySQL
Insert Data:

cursor.execute("""
INSERT INTO students (name, age, grade)
VALUES (%s, %s, %s)
""", ("Alice", 18, "A"))
conn.commit()
Select Data:

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)
Update Data:

cursor.execute("""
UPDATE students
SET grade = %s
WHERE name = %s
""", ("B", "Alice"))
conn.commit()
Delete Data:

cursor.execute("DELETE FROM students WHERE name = %s", ("Alice",))
conn.commit()
7. Exceptions and Error Handling
Handling Exceptions
Use try, except, else, and finally blocks to handle exceptions gracefully.


try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("No error occurred")
finally:
    print("Execution finished.")
8. Recursion
Recursion is when a function calls itself to solve smaller instances of the same problem. It’s important to have a base case to prevent infinite recursion.

Example of calculating factorial recursively:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
9. Advanced Topics
Lambda Functions
Lambda functions are small anonymous functions defined using the lambda keyword. They are typically used for short, one-line functions.

Example:


square = lambda x: x ** 2
print(square(5))  # Output: 25
List Comprehensions
List comprehensions provide a concise way to create lists from other iterables.

Example:


numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
Decorators
Decorators are a way to modify the behavior of a function or class. They are often used for logging, access control, caching, etc.

Example:


def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
Conclusion
These notes cover a wide range of topics in Python, from basics like variables, data types, and functions, to more advanced topics like file handling, MySQL, recursion, and decorators. This collection provides a strong foundation for students to tackle both theoretical and practical problems in Python programming.

By practicing these concepts through examples, students can build confidence and gain a deeper understanding of Python's capabilities. The application of these concepts in real-world scenarios such as working with databases, file handling, and data manipulation is key to mastering Python.
'''
def notes():

    """
    Returns the value of the global variable 'a'.

    This function retrieves and returns the content of the global variable 'a',
    which contains a comprehensive collection of Python programming notes. These
    notes cover a variety of topics in Python, providing a solid foundation for
    students to understand and apply Python concepts.
    """

    global a
    return a
x='''
1. Python Basics
Variables and Data Types
Python allows you to assign values to variables, and it automatically determines the data type based on the value assigned. Below are some examples of basic data types:


# Integers
x = 5
print(x)  # Output: 5

# Floats
y = 3.14
print(y)  # Output: 3.14

# Strings
name = "Alice"
print(name)  # Output: Alice

# Boolean
is_active = True
print(is_active)  # Output: True

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Tuple
coordinates = (4, 5)
print(coordinates)  # Output: (4, 5)

# Dictionary
person = {"name": "John", "age": 30}
print(person)  # Output: {'name': 'John', 'age': 30}

# Set
numbers = {1, 2, 3}
print(numbers)  # Output: {1, 2, 3}
2. Conditional Statements
If, Elif, Else
Conditional statements are used to make decisions in your code based on certain conditions.


x = 15

if x > 10:
    print("x is greater than 10")  # Output: x is greater than 10
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
3. Loops
For Loop
The for loop is used to iterate over a sequence (like a list, tuple, string, etc.).


fruits = ["apple", "banana", "cherry"]

# Iterating over a list with a for loop
for fruit in fruits:
    print(fruit)
Output:


apple
banana
cherry
While Loop
The while loop executes as long as the condition is True.


x = 1
while x <= 5:
    print(x)
    x += 1
Output:


1
2
3
4
5
4. Functions
Defining Functions
Functions help break down the code into reusable blocks.


def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
Return and Arguments
Functions can take arguments and return values.


def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8
5. Data Structures
Lists
Lists are ordered collections that can store a variety of data types.


# List with mixed data types
my_list = [1, 3.14, "hello", True]
print(my_list)  # Output: [1, 3.14, 'hello', True]

# List operations
my_list.append("new item")
print(my_list)  # Output: [1, 3.14, 'hello', True, 'new item']

my_list.remove(3.14)
print(my_list)  # Output: [1, 'hello', True, 'new item']
Tuples
Tuples are immutable, which means once defined, their values cannot be changed.


my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

# Accessing an element
print(my_tuple[1])  # Output: 2
Dictionaries
Dictionaries store data in key-value pairs.


person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing values
print(person["name"])  # Output: Alice

# Adding new key-value pair
person["job"] = "Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}
Sets
Sets store unique values and are unordered.


my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Adding to set
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
6. File Handling
Reading Files
To read a file, we use the open() function.


# Read from a file (Assuming a file "example.txt" exists)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
Writing to Files
You can write to a file using the write() method.


with open("example.txt", "w") as file:
    file.write("This is a test.")
Reading and Writing CSV Files
CSV (Comma Separated Values) files can be handled using the csv module.


import csv

# Writing to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Alice", 18, "A"])
    writer.writerow(["Bob", 17, "B"])

# Reading from CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
Output:


['Name', 'Age', 'Grade']
['Alice', '18', 'A']
['Bob', '17', 'B']
7. Exception Handling
Try and Except Block
You can handle exceptions using try and except blocks.


try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
Output:


Cannot divide by zero!
Finally Block
The finally block is always executed, even if there is an exception.


try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error!")
finally:
    print("This is executed no matter what!")
Output:


This is executed no matter what!
8. MySQL with Python
Connecting to MySQL Database
Here is how you can connect to a MySQL database using mysql-connector-python.


import mysql.connector

# Connecting to the database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

# Creating a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    grade VARCHAR(10)
)
""")

conn.commit()
CRUD Operations in MySQL
Insert Data:

cursor.execute("""
INSERT INTO students (name, age, grade)
VALUES (%s, %s, %s)
""", ("John", 18, "A"))
conn.commit()

print("Data inserted successfully!")
Read Data:

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)
Output:


(1, 'John', 18, 'A')
Update Data:

cursor.execute("""
UPDATE students
SET grade = %s
WHERE name = %s
""", ("B", "John"))
conn.commit()

print("Data updated successfully!")
Delete Data:

cursor.execute("DELETE FROM students WHERE name = %s", ("John",))
conn.commit()

print("Data deleted successfully!")
9. Recursion
Factorial Calculation
Recursion involves a function calling itself. Below is an example of calculating the factorial of a number using recursion.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
10. Lambda Functions
Lambda functions are small anonymous functions that can have any number of arguments but only one expression.


# Lambda function to find square of a number
square = lambda x: x ** 2
print(square(4))  # Output: 16
11. List Comprehensions
List comprehensions provide a concise way to create lists.


numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
Conclusion
These expanded notes and examples should give students a more detailed understanding of Python programming. Each topic is explained with practical examples that provide immediate feedback through outputs, helping students practice and learn. This approach enhances the learning experience and prepares students for exams, projects, or real-world programming scenarios.'''
def basics():

    """
    Basic notes for study
    
    This function does not take any arguments and does not do anything with the global variable x.
    It is only used to group the basic notes for study into a single function.
    """
    

    global x
    return x

df='''
Here's a concise guide covering MySQL, its core concepts, and essential commands. This should be helpful for understanding SQL basics and common operations!

MySQL Overview
MySQL is an open-source relational database management system (RDBMS) based on Structured Query Language (SQL). It’s used to manage databases and is known for its speed, reliability, and ease of use.

Basic Concepts
Database: A collection of tables that organize data in a structured way.
Table: Stores data in rows and columns.
Row: Represents a single record in a table.
Column: Represents an attribute or field in a table.
Primary Key: A unique identifier for each row in a table.
Foreign Key: A key used to link two tables together.
Basic MySQL Commands
1. Database Commands
Create a Database

CREATE DATABASE database_name;
Use a Database

USE database_name;
Show Databases

SHOW DATABASES;
Drop a Database

DROP DATABASE database_name;
2. Table Commands
Create a Table

CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);
Example:
sql
Copy code
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
Show Tables

SHOW TABLES;
Describe Table Structure

DESCRIBE table_name;
Drop a Table

DROP TABLE table_name;
3. Inserting Data
Insert Data into a Table

INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
Example:

INSERT INTO students (id, name, age) VALUES (1, 'Alice', 20);
4. Retrieving Data (SELECT Command)
Select All Data

SELECT * FROM table_name;
Select Specific Columns

SELECT column1, column2 FROM table_name;
Using WHERE Clause (Conditional Query)

SELECT * FROM table_name WHERE condition;
Example:

SELECT * FROM students WHERE age > 18;
Using ORDER BY (Sorting Data)

SELECT * FROM table_name ORDER BY column_name ASC|DESC;
Using LIMIT (Restricting Number of Rows Returned)

SELECT * FROM table_name LIMIT number;
5. Updating Data
Update Data in a Table

UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
Example:

UPDATE students SET age = 21 WHERE name = 'Alice';
6. Deleting Data
Delete Data from a Table

DELETE FROM table_name WHERE condition;
Example:

DELETE FROM students WHERE age < 18;
7. Constraints
Primary Key: Ensures that each record has a unique value for this field.

CREATE TABLE table_name (
    column_name datatype PRIMARY KEY
);
Foreign Key: Links two tables together.

CREATE TABLE orders (
    order_id INT,
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
Not Null: Ensures that a column cannot have a NULL value.

CREATE TABLE table_name (
    column_name datatype NOT NULL
);
8. Aggregate Functions
COUNT(): Counts the number of rows in a table.

SELECT COUNT(*) FROM table_name;
SUM(): Calculates the sum of a numeric column.

SELECT SUM(column_name) FROM table_name;
AVG(): Calculates the average value of a numeric column.

SELECT AVG(column_name) FROM table_name;
MIN() and MAX(): Finds the minimum and maximum values.

SELECT MIN(column_name) FROM table_name;
SELECT MAX(column_name) FROM table_name;
9. Grouping Data
GROUP BY: Groups rows that have the same values in specified columns into summary rows.

SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;
10. Joins
Joins are used to combine rows from two or more tables based on a related column.

INNER JOIN: Returns rows with matching values in both tables.

SELECT a.column_name, b.column_name
FROM table1 a
INNER JOIN table2 b ON a.common_field = b.common_field;
LEFT JOIN (or LEFT OUTER JOIN): Returns all rows from the left table, even if there’s no match in the right table.

SELECT a.column_name, b.column_name
FROM table1 a
LEFT JOIN table2 b ON a.common_field = b.common_field;
RIGHT JOIN: Returns all rows from the right table, even if there’s no match in the left table.

SELECT a.column_name, b.column_name
FROM table1 a
RIGHT JOIN table2 b ON a.common_field = b.common_field;
Common Data Types in MySQL
INT: Integer numbers (whole numbers).
FLOAT/DOUBLE: Floating-point numbers.
CHAR(size): Fixed-length character strings.
VARCHAR(size): Variable-length character strings.
DATE: Date in YYYY-MM-DD format.
TIME: Time in HH:MM:SS format.
DATETIME: Date and time in YYYY-MM-DD HH:MM:SS format.
BOOLEAN: True or False values (stored as 1 or 0).
SQL Clauses and Keywords
DISTINCT: Used to select unique values.

SELECT DISTINCT column_name FROM table_name;
IN: Checks if a value is within a set of values.
sql
Copy code
SELECT * FROM table_name WHERE column_name IN (value1, value2, ...);
BETWEEN: Checks if a value falls within a range.
sql
Copy code
SELECT * FROM table_name WHERE column_name BETWEEN value1 AND value2;
LIKE: Used for pattern matching.
sql
Copy code
SELECT * FROM table_name WHERE column_name LIKE 'pattern';
IS NULL: Checks for NULL values.

SELECT * FROM table_name WHERE column_name IS NULL;
Example of a Simple SQL Database Operation
Assume we have two tables: students and courses.

Create Tables


CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
Insert Data


INSERT INTO students (id, name, age) VALUES (1, 'Alice', 20);
INSERT INTO students (id, name, age) VALUES (2, 'Bob', 22);

INSERT INTO courses (course_id, course_name, student_id) VALUES (101, 'Math', 1);
INSERT INTO courses (course_id, course_name, student_id) VALUES (102, 'Science', 2);
Retrieve Data with Join


SELECT students.name, courses.course_name
FROM students
INNER JOIN courses ON students.id = courses.student_id;
Output:


name   | course_name
--------------------
Alice  | Math
Bob    | Science
This guide should provide a strong foundation for understanding MySQL and SQL commands, and help you confidently execute basic and intermediate database operations!'''
def mysqlnotes():

    """
    Returns an overview guide about MySQL, covering core concepts and essential commands.
    The guide is stored in a global variable 'df'.
    """

    global df
    return df

