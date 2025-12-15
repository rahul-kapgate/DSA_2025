num = int(input("Enter a number : "))

i = 2

while i < num:
    if(num%i == 0):
        print("Not a prime number")
        break
    else:
        print("Prime number") 
        break
i += 1




# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime) 
