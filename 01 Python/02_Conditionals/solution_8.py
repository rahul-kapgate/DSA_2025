password = "12345"
# password = "123456"
# password = "1234567890"
# password = "123456789011"

lenght = len(password)

if lenght < 6:
    print("Week")
elif lenght <= 10:
    print("Medium")
elif lenght > 10:
    print("Strong")        