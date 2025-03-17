# items = ["apple", "banana", "orange", "apple", "mango"]

# count = 0

# for i in items:
#     count = 0
#     for j in items:
#         if i == j:
#             count += 1
# if count >= 2:
#     print(i)


items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)
            



   