age = int(input("Enter Your age : "))
# day = "Wednesday"
day = "Monday"
price_for_adult = 12
price_for_childers = 8
disscount = 2

if age < 18 and day == "Wednesday":
    print(price_for_childers - disscount)
elif age < 18:
    print(price_for_childers)
elif age >= 18 and day == "Wednesday":
    print(price_for_adult - disscount)
else:
    print(price_for_adult)



# age = 26
# day = "Wednesday"

# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     # price = price - 2
#     price -= 2

# print("Ticket price for you is $",price)