# In Python, strings are sequences of characters enclosed in single quotes ('), 
# double quotes ("), or triple quotes (''' or """) for multi-line strings. Strings are immutable, 
# meaning they cannot be changed after creation.

# Using single or double quotes
s1 = 'Hello'
s2 = "World"

# Multi-line strings using triple quotes
s3 = '''This is
a multi-line
string'''



# Indexing ([]) & Slicing ([:])


s = "Python"
print(s[0])   # 'P' (First character)
print(s[-1])  # 'n' (Last character)
print(s[1:4]) # 'yth' (Substring from index 1 to 3)

# String Length (len())

s = "Hello"
print(len(s))  # Output: 5

# String Iteration

for char in "Python":
    print(char)


#     Method	Description
# lower()	Converts to lowercase
# upper()	Converts to uppercase
# strip()	Removes spaces from start and end
# replace(old, new)	Replaces substring
# split(delim)	Splits string into a list
# join(iterable)	Joins elements with a separator
# find(substring)	Finds index of substring
# startswith(prefix)	Checks if string starts with a given substring
# endswith(suffix)	Checks if string ends with a given substring

s = "  Hello Python  "
print(s.strip())  # "Hello Python"

print(s.upper())  # "  HELLO PYTHON  "

print(s.replace("Python", "World"))  # "  Hello World  "

print("apple,banana,mango".split(","))  # ['apple', 'banana', 'mango']

print("-".join(["Python", "is", "fun"]))  # "Python-is-fun"

print(s.find("Python"))  # 8

# String Formatting

# Using f-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.") 

# Using .format()
print("My name is {} and I am {} years old.".format(name, age))
