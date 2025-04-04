def my_fun(*args):
    sum = 0
    for i in args:
        sum += i

    return sum    


print(my_fun(1,2,3,4,5,6,7,8,9,10))    