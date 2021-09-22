# Python for Numerical Analysis 101
# Homework
# Instructor: Evelyn J. Boettcher, DiDacTex, LLC
# Week 2 Lesson 1

# Author: Grace Metzgar
# Date: 20210920

# Pr 1

# Create a python script ***file*** (example: Pr1_WK2.py), that when executed prints to screen.

print("Hello problem 1 from Week 2 Lesson 1.")

# Pr 2

# Explain why you should ALWAYS have a .gitignore file in your repo.

# Pr 3

# Using `open` , create a new file that records user input (min 1, max 4 inputs) and then opens that files and APPENDS the following "Received User Input"

my_file = open('pr1_wk2.txt', 'a')
my_file.write(input("Enter name: "))
my_file.write("\nReceived User Input\n")
my_file.close()


## Pr 4

# repeat # 3 with a `with`

with open('pr1_wk2.txt', 'a') as my_file:
    my_file.write(input("Enter age: "))
    my_file.write("\nReceived User Input\n")

## Pr 5

# Create a new git repo in github.
# Populate it with typical files and directories (.gitignore and README.md)
# Commit your changes.
# Push it to your repository

# Sidebar

# Why have a github account?

# Industry and some government jobs check your github account to see if you really do know that software language.
# It free and a nice place to store software you used and like.
# You can help contribute to open data!