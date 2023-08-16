from math import pi

#program to find the area of a circle
def circle_area(radius):
    if radius < 0:
        raise ValueError("The radius cannot be negative.")

    if type(radius) not in [float, int]:
        raise TypeError("The radius must be of type float or integer")
        print("The radius must be of type float or integer")

    return pi*(radius**2)

print("hello python - circle2.py file. this is to indicate that the code in the file, located remotely on github, has been executed")
