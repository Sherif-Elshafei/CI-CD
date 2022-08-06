from math import pi

#program to find the area of a circle
def circle_area(radius):
    if type(radius) not in [float, int]:
        raise TypeError("radius is not a number")
    
    if radius<0:
        raise ValueError("radius cannot be less thn zero")

    return pi*(radius**2)

#print(circle_area(radius))


