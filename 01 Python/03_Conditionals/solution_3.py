marks = int(input("Enter your marks : "))
Grades = ""

if marks <= 100 and marks >= 90:
    Grades = "A"
elif marks <= 89 and marks >= 80:
    Grades = "B"    
elif marks <= 79 and marks >= 70:
    Grades = "C"    
elif marks <= 69 and marks >= 60:
    Grades = "D"
else:
    Grades = "F" 

print("Your grades is:",Grades)           



# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("Grade: ", grade)