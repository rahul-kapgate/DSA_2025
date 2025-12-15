# In Python, a set is an unordered collection of unique elements. 
# It is useful when you need to store distinct values and perform operations like union, 
# intersection, and difference.


from math import cos


my_set = {1,2,3,4,5}
my_empty_set = {} 
empty_set = set()
another_set = set([1, 2, 3, 4, 5])

print(my_set)
print(my_empty_set)
print(empty_set)

my_set.add(6)  # Adds 6 to the set
my_set.add(3)  # Duplicate, won't be added

my_set.remove(2)  # Removes 2, raises an error if not found
my_set.discard(10)  # Does nothing if 10 is not in the set


popped_element = my_set.pop()  # Removes a random element
print(popped_element)


A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Output: {1, 2, 3, 4, 5}
print(A.union(B))  # Same as above

print(A & B)  # Output: {3}
print(A.intersection(B))  # Same as above

print(A - B)  # Output: {1, 2} (Elements in A but not in B)
print(A.difference(B))  # Same as above


print(A ^ B)  # Output: {1, 2, 4, 5} (Elements in A or B, but not both)
print(A.symmetric_difference(B))  # Same as above


print(1 in A)  # Output: True
print(10 in A)  # Output: False

A.update(B)  # Adds all elements of B to A
A.clear()  # Removes all elements from A

new_set = {1,2,3,3} #duplicated simple ignored 
print(new_set)  #{1, 2, 3}
