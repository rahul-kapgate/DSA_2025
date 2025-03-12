# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.

my_dist = {
    "name" : "Rahul",
    "age" : 23,
    "city" : "Bnaalore",
    "profession" : "Software Engineer",
    "isPresent" : True
}

print(my_dist)

# Accessing Items
print(my_dist["name"])
print(my_dist.get("age"))

print(len(my_dist))
print(type(my_dist))

student_dict = dict(name="Rahul", age=23, city="Bangalore", profession="Software Engineer", isPresent=True)
print(student_dict)

# keys() method will return all the keys of the dictionary
all_keys = my_dist.keys()
print(all_keys)

my_dist["gender"] = "male"
print(all_keys)

# values() method will return all the values of the dictionary
all_values = my_dist.values()
print(all_values)

my_dist["age"] = 24 
print(all_values)

# items() method will return all the key value pairs of the dictionary
all_items = my_dist.items()
print(all_items)

if "name" in my_dist:
    print("Yes, 'name' is one of the keys in the my_dist dictionary")

print("\n")

# change item value
my_dist["city"] = "Mumbai"
print(my_dist)    

#update() method will update the dictionary with the specified key-value pairs
my_dist.update({"city": "Bangalore", "age": 23})
print(my_dist)

# nested dictionary
my_family = {
    "child1" : {
        "name" : "Rahul",
        "age" : 23
    },
    "child2" : {
        "name" : "Rohan",
        "age" : 25
    },
    "child3" : {
        "name" : "Raj",
        "age" : 30
    }
}


print(my_family)

# loop through a dictionary
for key in my_dist:
    print(key)

for values in my_dist:
    print(my_dist[values])

for key , values in my_dist.items():
    print(key,"=", values)        

# Method	   Description
# clear()	   Removes all the elements from the dictionary
# copy()	   Returns a copy of the dictionary
# fromkeys()   Returns a dictionary with the specified keys and value
# get()	       Returns the value of the specified key
# items()	   Returns a list containing a tuple for each key value pair
# keys()	   Returns a list containing the dictionary's keys
# pop()	       Removes the element with the specified key
# popitem()	   Removes the last inserted key-value pair
# setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	   Updates the dictionary with the specified key-value pairs
# values()	   Returns a list of all the values in the dictionary