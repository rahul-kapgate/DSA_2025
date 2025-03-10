# 1. open file 

file = open("file1.txt", "r")
contant = file.read()
print(contant)
file.close()

file = open("example.txt", "w")  # Overwrites existing content
file.write("Hello, World!\nThis is Python.")
file.close()

file = open("example.txt", "a")  # Appends content
file.write("\nAppending a new line.")
file.close()


with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # No need to call file.close()


import os
os.remove("example.txt")  # Deletes the file
