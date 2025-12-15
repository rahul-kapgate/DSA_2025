fruits_color = ["Green","Yellow","Brown"]

for index, value in enumerate(fruits_color, start=1):
    print(index,value)

selected_color = int(input("Select the color of fruit [1,2,3] : "))


if selected_color == 1:
    print("Unripe")
elif selected_color == 2:
    print("Ripe")
elif selected_color == 3:
    print("Overripe") 
else:
    print("Enter valid color")          



# fruit = "Banana"
# color = "Yellow"

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("OverRipe")
