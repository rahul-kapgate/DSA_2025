year = 2100

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year")
        else:
            print("NOT a leap year")
    else:
        print("Leap year")    


# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print( year, " is a leap year")
# else:
#     print(year, "is NOT a leap year")        