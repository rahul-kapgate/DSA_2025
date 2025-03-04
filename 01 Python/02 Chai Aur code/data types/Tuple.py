# Tuple in Python
# A tuple is a built-in Python data structure used to store an ordered, immutable collection of elements. 
# Tuples are similar to lists but cannot be modified after creation.

# Key Features of Tuples
# Ordered → Elements maintain their sequence.
# Immutable → Cannot change, add, or remove elements after creation.
# Heterogeneous → Can store different data types.
# Indexable → Elements can be accessed using indexes.
# Faster than lists → Since they are immutable, they have better performance in certain cases.

empty_tuple = ()
num_tuple = (1,2,3,45,67,8,89,47)
mixed_tuple = (1,2,"three",4, "five",[1,6,9])
single_element_tuple = (42,)  # A single-element tuple must have a trailing comma
converted_tuple = tuple([1, 2, 3])  # Creating tuple from a list

print(empty_tuple)
print(num_tuple)
print(mixed_tuple)
print(single_element_tuple)
print(converted_tuple)

print(num_tuple[0])

# num_tuple[0] = 2     TypeError: 'tuple' object does not support item assignment

# However, if a tuple contains mutable elements (like lists), those elements can be modified.

mutable_tuple = (1, [2, 3], 4)
mutable_tuple[1].append(5)
print(mutable_tuple)


##############  Tuple Operations
# Operation	         Example	            Output
# Concatenation	    (1, 2) + (3, 4)	      (1, 2, 3, 4)
# Repetition	    ("Hi",) * 3	          ('Hi', 'Hi', 'Hi')
# Membership	    3 in (1, 2, 3)	       True
# Length	       len((1, 2, 3))	        3
# Index	          (10, 20, 30).index(20)	1
# Count	          (1, 2, 2, 3).count(2)	    2