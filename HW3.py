# Python for Data Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Week 1: Lecture 3


## HW

# Write a conditional expression statement with, "if, elif and else." to check if my_string = "Hello World" is a string

my_string = "Hello World"
if type(my_string) == str:
    print("string")
else:
    print("not a string")

# Write a list comprehension that returns all the keys in a dictionary whose associated values are greater than zero.
my_dict = {'aa': 11, 'cc': 33, 'LESS Than': -55, 'bb': 22}

# Output should be a list   
my_list = [x for x in my_dict.values() if x > 0]
print(my_list)

# Write a list comprehension that produces even integers from 0 to 10.
# Use a `for` statement to iterate over those values and print results to screen.

num_list = [x for x in range(0, 11) if x % 2 == 0]
print(num_list)

# Write a list comprehension that iterates over two lists and produce all the combinations of items from the lists.

list1 = range(0, 3)
list2 = range(5, 8)
com_list = [(x, y) for x in list1 for y in list2]
[print(com_list)]

# Using `break`, write a `while` statement that prints integers from zero to 5.

i = 0
while i < 20:
    print(i)
    i += 1
    if i > 5:
        break

#   Using `continue` , write a `while` statement that processes only even integers from 0 to 10. Note: `%` is themodulo operator.

i = -1
while i < 10:
    i += 1
    if i % 2 == 0:
        print(i)
        continue
    
    
 