# Pet = "Dog"
# Pet = "Cat"

# pet_age = 1

# if pet_age < 2:
#     print("Puppy", Pet, "food")
# elif pet_age > 6:
#     print("Senior", Pet, "food")

pet = "Dog"  # Change to "Cat" to test for cats
pet_age = 1   # Change this value to test different ages

if pet == "Dog":
    if pet_age < 2:
        print("Puppy Dog Food")
    elif pet_age > 6:
        print("Senior Dog Food")
    else:
        print("Adult Dog Food")

elif pet == "Cat":
    if pet_age < 2:
        print("Kitten Cat Food")
    elif pet_age > 5:
        print("Senior Cat Food")
    else:
        print("Adult Cat Food")

else:
    print("Unknown pet type")
