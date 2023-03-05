#Ask the user to enter a shape: circle, square or triangle. 
#Then ask for the information appropriate to the shape i.e. radius, or side or height, 
#base etc and use these values to calculate the correct area for the shape and output 
#a suitable message. eg ‘the area of the circle is 23’

input1 = input("This program calculates the area of a circle, square or triangle. Choose the shape you require: ")
from math import pi
#Area of a square
if input1 == "square":
    side = int(input("Enter the length of the side: "))
    area = side ** 2
#Area of a circle
elif input1 == "circle":
        r = int(input("Enter the length of the radius: "))
        area = pi * r ** 2 
#Area of a triangle
elif input1 == "triangle":
        base = int(input("Enter the width of the base: "))
        height = int(input("Enter the height: "))
        area = 0.5 * base * height
#Error message
else:
    print ("Select a valid shape, remember to type in all lower case")

print ("The area of the shape is %.2f" % area) #gives answer to 2 decimal places


