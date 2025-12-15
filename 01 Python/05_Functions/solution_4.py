def circle(radius):
    area = (22/7)*radius*radius
    circumfrance = 2* (22/7)*radius

    return area, circumfrance

a, c = circle(10)

print(a)
print(c)