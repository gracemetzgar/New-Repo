# Author: Grace Metzgar
# Date: 20210917

# Python for Data Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Week 1: Lecture 4

# Write a function that takes a single argument, prints the value of the argument, and returns the argument as a string.

def str_function(x):
    print(x)
    return str(x)

if type(str_function(10)) == str:
    print("string")
else:
    print("not a string")

# Write a function that takes a variable number of arguments and prints them all.

def variable_function(*values):
    for x in  values:
        print(x)
        
variable_function(1, 2, 3, 4, 5)

# Write a function that prints the names and values of keyword arguments passed to it.

def key_function(**arguments):
    for key in arguments:
        print(key, arguments[key])
        
key_function(a = 1, b = 2, c = 3)

# Write a python script (file) that prints your name as all lower case, upper case and proper capitalization. 

def name_function(my_name):
    print(my_name.upper())
    print(my_name.lower())
    print(my_name.title())
     
name_function("grace metzgar")
