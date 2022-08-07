from math import pi

#program to find the area of a circle
def circle_area(radius):
<<<<<<< HEAD
    if type(radius) not in [float, int]:
        raise TypeError("radius is not a number")
    
    if radius<0:
        raise ValueError("radius cannot be less thn zero")

    return pi*(radius**2)

#print(circle_area(radius))
=======
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    if type(radius) not in [float, int]:
        raise TypeError("The radius must be of type float or integer")
    return pi*(radius**2)


>>>>>>> 725a7bc0991c69c317b7778cd6ad3f5bb40b4709


