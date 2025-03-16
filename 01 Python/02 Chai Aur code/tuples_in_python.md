# **Tuples in Python**  

A **tuple** is an **immutable** (unchangeable) and **ordered** collection in Python that allows you to store multiple items in a single variable.

---

## **1. Creating a Tuple**
You can create a tuple using parentheses `()` and separate elements with commas.

```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
```

### **Tuple with Different Data Types**
```python
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)  # Output: (1, 'Hello', 3.14, True)
```

### **Tuple with One Element**
To create a single-element tuple, you **must** include a trailing comma.

```python
single_element_tuple = (5,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

not_a_tuple = (5)
print(type(not_a_tuple))  # Output: <class 'int'>
```

---

## **2. Accessing Tuple Elements**
Tuples support **indexing** and **slicing** like lists.

```python
numbers = (10, 20, 30, 40, 50)

# Accessing elements
print(numbers[0])  # Output: 10
print(numbers[-1])  # Output: 50 (last element)
```

### **Tuple Slicing**
```python
print(numbers[1:4])  # Output: (20, 30, 40)
print(numbers[:3])   # Output: (10, 20, 30)
print(numbers[::2])  # Output: (10, 30, 50)
```

---

## **3. Tuple Immutability**
Tuples **cannot** be modified after creation.

```python
numbers[1] = 25  # ❌ This will raise an error
```
However, you can **reassign** a variable to a new tuple.

```python
numbers = (10, 25, 30, 40)  # ✅ This is allowed
```

---

## **4. Tuple Methods**
Tuples have only two built-in methods:  
- `count()` → Returns the number of times a value appears.  
- `index()` → Returns the index of the first occurrence of a value.

```python
t = (1, 2, 3, 2, 4, 2)

print(t.count(2))   # Output: 3
print(t.index(3))   # Output: 2 (position of first occurrence)
```

---

## **5. Tuple Packing & Unpacking**
### **Packing**
Packing means putting multiple values into a tuple.

```python
person = ("Alice", 25, "Engineer")
```

### **Unpacking**
Unpacking means extracting values into separate variables.

```python
name, age, job = person
print(name)  # Output: Alice
print(age)   # Output: 25
print(job)   # Output: Engineer
```

**Using `*` for Variable-length Unpacking**
```python
numbers = (1, 2, 3, 4, 5)
a, *b, c = numbers

print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5
```

---

## **6. Tuple vs List**
| Feature  | Tuple | List |
|----------|-------|------|
| **Mutable?** | ❌ No (Immutable) | ✅ Yes (Mutable) |
| **Syntax** | `()` | `[]` |
| **Performance** | ✅ Faster | ❌ Slower |
| **Memory Efficient?** | ✅ Yes | ❌ No |

---

## **7. Tuple Operations**
### **Concatenation**
```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
result = t1 + t2
print(result)  # Output: (1, 2, 3, 4, 5, 6)
```

### **Repetition**
```python
t = (1, 2) * 3
print(t)  # Output: (1, 2, 1, 2, 1, 2)
```

### **Membership Test**
```python
t = (10, 20, 30)
print(20 in t)  # Output: True
```

---

## **8. Converting Between Tuple & List**
### **Tuple → List**
```python
t = (1, 2, 3)
l = list(t)
l.append(4)
t = tuple(l)
print(t)  # Output: (1, 2, 3, 4)
```

### **List → Tuple**
```python
l = [1, 2, 3]
t = tuple(l)
print(t)  # Output: (1, 2, 3)
```

---

## **9. Tuple with `for` Loop**
```python
colors = ("red", "green", "blue")
for color in colors:
    print(color)
```

---

## **10. When to Use Tuples?**
- When you **don't** want data to change (e.g., database records, coordinates).
- When you need **faster performance** (tuples are faster than lists).
- When you want to use a sequence as a **dictionary key** (lists can't be keys).

---

## **11. Named Tuple (from `collections` module)**
Named tuples provide **better readability** by allowing element access by name instead of index.

```python
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "job"])
p1 = Person(name="Alice", age=25, job="Engineer")

print(p1.name)  # Output: Alice
print(p1.age)   # Output: 25
```

---

## **Conclusion**
- Tuples are **immutable**, meaning they **cannot be changed** after creation.
- They are **faster and memory-efficient** compared to lists.
- Useful for storing **fixed collections of items** like coordinates, database records, etc.
