""" Help on Names Module

NAME: 
names.py

DESCRIPTION:
	this module helps to 

"""


#area of a square
def area_of_square(l):
	#where l = the length of the sides of the square
	return l ** 2

#area of a rectangle
def area_of_rectangle(l, b):
	return l * b

#area of a triangle
def area_of_triangle(h, b):
	return (0.5 * b) * h

#perimeter of a square
def perimeter_of_square(l):
	#where l is the length of the sides of the square
	return 4 * l

#perimeter of a rectangle
def perimeter_of_rectangle(l, w):
	return (2*l) + (2*w)


#perimeter of a triangle
def perimeter_of_triangle(a, b, c):
	return a + b + c

def perimeter_of_trapezoid(a, b1, b2, c):
	return a + b1 + b2 + c

#perimeterof a parallelogram
def perimeter_of_parallelogram(a, b):
	#
	 return (2*a) + (2*b)




##volume
#volume of a cume
def volume_of_cube(l):
	return l ** 3

#volume of a prism or cylinder
#a is the area of the base
#h is the height
def volume_of_prism(a, h):
	return a * h

def volume_of_cylinder(a, h):
	return a * h

#volume of a prism or cylinder
#a is the area of the base
#h is the height
def volume_of_pyramid(a, h):
	return 1/3 * (a * h)


def volume_of_cylinder(a, h):
	return 1/3 * (a * h)


	

