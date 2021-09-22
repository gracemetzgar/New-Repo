# Python for Data Analysis and Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Week 1: Lecture 2


## 1 Lists
# Create an empty list. Append 4 strings to the list. Then pop one item off the end of the list.

my_list = []
my_list.append("hello")
my_list.append("hola")
my_list.append("hallo")
my_list.append("bonjour")
my_list.pop()

print(my_list)

## 2 Dictionaries
# Create a dictionary using with a zip and two lists
# Add to this dictionary using the key "HW2" with value "Done"
# Define a dictionary using both string literals   and variables containing strings.

course = ["math", "english", "history"]
grade = ["A", "B", "F"]
my_dict = dict(zip(course, grade))
print(my_dict)

my_dict["HW2"] = "Done"
print(my_dict)


## 3 Strings
# Use a literal to create a string containing:
  # a single quote,
  # a double quote,
  # both a single and double quote.

print("hello my name is 'Grace'")
print('hello my name is "Grace"')
print('"hello" my name is \'Grace\'')
## 4 Strings Multi-line
# Write a string literal that spans multiple lines.

my_string = "Hola me llamo Grace\ny me gusta comer uvas\nadios."
print(my_string)

## 5 `join`

# Use the string `join` operation to create a string that contains a colon as a separator.

my_list2 = ["one", "two", "three"]
new_string = ':'.join(my_list2)
print(new_string)

## 6 String Format.
# Use string formatting to produce a string containing your last and first names, separated by a comma.

first = 'Grace'
last = 'Metzgar'
full = '%s, %s' % (last, first)
print(full)