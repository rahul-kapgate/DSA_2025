def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i



for num in even_generator(10):
    print(num)



    # The yield keyword makes this function a generator, 
    # meaning it doesn't return all values at once but produces them one by one when iterated over.