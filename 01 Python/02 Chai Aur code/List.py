# list (Array)

my_list = [1, 2, 3, 4, 5]
print(my_list)

item_list = ['apple', 'banana', 'cherry']
list_of_list = [1, 'apple', 2, 'banana', 3, 'cherry']

empty_list = []
print(empty_list)

print(type(my_list))

list_constructor = list((1,2,3,4,5))


# Access Items  in list
print(my_list[0])
print(my_list[1])

print(my_list[-1])

print(my_list[2:5])
print(my_list[:4])
print(my_list[2:])
print(my_list[-4:-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
    

 # change item value
thislist[1] = "blackcurrant"
print(thislist)   


# insert new item
thislist.insert(2, "watermelon")
print(thislist)

# append
thislist.append("orange")   
print(thislist)

# extend  =>  To append elements from another list to the current list, use the extend() method.
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#The extend() method does not have to append lists, you can add any 
# iterable object (tuples, sets, dictionaries etc.).


# remove item =>  remove() method removes the first occurrence
thislist.remove("mango")
print(thislist)

# pop() method removes the specified index, (or the last item if index is not specified)
thislist.pop(1)
print(thislist)

#the pop() method removes the last item.
thislist.pop()
print(thislist)


# The del keyword also removes the specified index:
del thislist[0]
print(thislist)

#The clear() method empties the list.
# The list still remains, but it has no content.
thislist.clear()
print(thislist)

# The del keyword can also delete the list completely.
del thislist
# print(thislist)  # this will cause an error because "thislist" no longer exists.


# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list