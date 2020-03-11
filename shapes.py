"""
This is the for the shapes area calculations. 
Description: You should write functions for calculating the area of a given shape. 
The program should ask for user-input and ask for which shape the user want to calculate
 the area for (for. ex.: "Introduce the kind of shape you want 
to calculate the area for choose from these: circle/rectangle/triangle/square")
 Then based on the user input you should ask for the dimensions of the chosen shape 
 (for ex.: if circle, then ask for the radius; if rectangle ask for width and height)
Requirements:
- you should create a main function which handles the first user input (choosing between the supported shapes) and handles each case differently
- you should create separate functions for calculating area of a given shape and return it (for ex.: calc_area_circle; calc_area_rectangle)
- the main function should handle the different shapes (if-else statement) ask for more user input (for ex.: if rectangle ask for width and height) and call the coresponding area calculation functions with the user input
Note:
- ha jol csinaljatok minden a `main` functionbe tortenik (function-bodyba tortenik minden logike) es function-on kivul csak a function meghivas talalhato pl.: main()  
""" 
import math

def circle(r):
	aria = (r * r) * math.pi
	return aria

def triangle(width, height):
	aria = (width * height)/2
	return aria

def rectangle(width, height):
	aria = width * height
	return aria

def main():
	shape = input("Enter the requested shape: ")
	
	if shape == "circle":
		print("Calculate circle aria")
		r = float(input("Enter the radius lenght: "))
		aria = circle(r)
		print("The circle aria is: {}".format(aria))
	elif shape == "square":
		print("Calculate square aria")
		side = float(input("Enter the side lenght: "))
		aria = rectangle(side, side)
		print("The square aria is: {}".format(aria))
	elif shape == "triangle":
		print("Calculate triangle aria")
		width = float(input("Enter the width lenght: "))
		height = float(input("Enter the height lenght: "))
		aria = triangle(width, height)
		print("The triangle aria is: {}".format(aria))
	elif shape == "rectangle":
		print("Calculate rectangle aria")
		width = float(input("Enter the width lenght: "))
		height = float(input("Enter the height lenght: "))
		aria = rectangle(width, height)
		print("The rectangle aria is: {}".format(aria))
	else:
		print(" Wrong shape input {} .. prostule ".format(shape))

main()

