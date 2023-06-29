'''
exercise 1:

create a function that takes in the radius of a circle and calculates the area. π * r^2. 

------------

excercise 2:

Convert Celcius to Farenheight and then a second funtion to convert farenheight to cel≈
'''


def area_of_circle(radius):
    answer = 3.14 * (radius**2)

    return (answer)


print(area_of_circle(54))


def cel_to_fahr(cel):
    answer = (cel * 9/5) + 32
    return (answer)


print(cel_to_fahr(42))


def fahr_to_cel(fahr):
    answer = (fahr - 32) * 5/9
    return (answer)


print(fahr_to_cel(42))
