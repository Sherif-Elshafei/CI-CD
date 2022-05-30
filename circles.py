from math import pi

#program to find the area of a circle
def circle_area(radius):
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    if type(radius) not in [float, int]:
        raise TypeError("The radius must be of type float or integer")
    return pi*(radius**2)




