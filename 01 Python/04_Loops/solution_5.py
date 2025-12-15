my_string = "chaiaurcode"

for char in my_string:
    count = 0
    for char1 in my_string:
        if(char == char1):
            count += 1

    if count < 2:
        print(char)
        break        
