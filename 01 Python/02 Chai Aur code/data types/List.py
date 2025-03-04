# List in Python
# A list in Python is a built-in data structure that is used to store an ordered, mutable collection of elements. 
# Lists can contain elements of different data types, including integers, floats, strings, and even other lists.

## Key Features of Lists
# Ordered → Elements maintain their sequence.
# Mutable → You can modify the list (add, remove, change elements).
# Heterogeneous → Can store different data types in the same list.
# Indexable → Elements can be accessed using indexes.
# Dynamic → Can grow or shrink as needed.

empty_list = []
num_list = [1,2,3,4,5]
mixed_list = ["rahul", 1, 1.45, ["first", "second"]]
range_list = list(range(5))

print(empty_list)
print(num_list)
print(mixed_list)
print(range_list)

print(num_list[0])

num_list[0] = 11
print(num_list)

##### List Methods
# Method	           Description	             Example
# append(x)	           Adds x to the end	    lst.append(10)
# extend(iterable)	Adds multiple elements	    lst.extend([4, 5, 6])
# insert(i, x)	    Inserts x at index i	    lst.insert(1, "hello")
# remove(x)	     Removes first occurrence of x	lst.remove(3)
# pop(i)	    Removes and returns element     lst.pop(2) 
#                  at i(i is a index)	
# index(x)	        Returns the index of x	    lst.index(5)  
# count(x)	      Counts occurrences of x	    lst.count(2)  
# sort()	        Sorts the list	            lst.sort()
# reverse()	        Reverses the list	       lst.reverse()         

lst = [];
print(lst)

lst.append(1)
print(lst)

lst.extend([2,3,4,5,6,7,7,7])
print(lst)

lst.insert(1, "new El")
print(lst)

lst.remove(4)
print(lst)

popEl = lst.pop(0)
print(lst)
print(popEl)

indexEl = lst.index(5)
print(lst)
print(indexEl)

countEl = lst.count(7)
print(lst)
print(countEl)

my_list = [1,23,5,8,0,43,4564,23,24,23,23,53,45,3]
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)