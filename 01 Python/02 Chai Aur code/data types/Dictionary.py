# Dictionary in Python
# A dictionary in Python is a built-in data structure that stores data in key-value pairs. 
# It is unordered, mutable, and allows for fast lookup of values based on keys.

# Key Features of Dictionaries
# Key-Value Pairs → Data is stored as {key: value} pairs.
# Unordered (Before Python 3.7) → No fixed order (but from Python 3.7+, dictionaries maintain insertion order).
# Mutable → Values can be changed, added, or removed.
# Keys Must Be Unique → Duplicate keys are not allowed.
# Keys Must Be Immutable → Keys can be str, int, tuple, etc., but not lists or dictionaries.

# A dictionary in Python is an unordered collection of key-value pairs. 
# It is defined using curly braces {} and allows fast lookups, insertions, and deletions.

my_dict = {}    #empty dictionary

person = {
    "name" : "Rahul",
    "age": 23,
    "city" : "Bangalore"
}

print(person)

## accsessing Dictionary values
print(person["name"])
print(person.get("age"))  #get() is safer because it returns None instead of an error if the key does not exist.

# modifying dictionary

# Updating values  
person["name"] = "Rahul Kapgate"

#add new key-value pair
person["job"] = "Software Engineer"

print(person)


## Removing data
del person["age"]   #delete a key
print(person)

name = person.pop("name") #remove and return value
print(name)


# Looping 
for key, value in person.items():
    print(key, "::", value)