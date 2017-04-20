'''
Author : Nilesh Chaturvedi
Last updated : 20th April 2017

Description : This routine uses gradient descent method to return the point of minima of a polynomial. 
'''

import numpy as np
import math

def grad(coefs, x): 
	# Returns value of gradient at point x for the function with given co-efficients
	grad = []
	[grad.append(int(i)) for i in coefs]

	poly_obj= np.poly1d(grad)
	grad_vec = np.polyder(poly_obj)

	grad_val = (np.poly1d(grad_vec))(x)

	return(grad_val)

def main():

	degree = input("Highest Degree of the polynomial : ")
	coefs = input("Enter the co-efficient of each term starting" 
		"with highest degree first (separate them by spaces) : ").split()
	descent_rate = float(input("Rate of descent : "))
	starting_point = float(input("Starting point : "))

	permissible_error = 0.00000000000001
	gradient = 0
	x0 = starting_point
	xn = 0
	error = float('inf')

	while (error >= permissible_error):
		x0=xn
		gradient = grad(coefs, x0)
		xn = x0 - (descent_rate * gradient)
		error = abs(xn - x0)

	print(" Point of minima is : {}".format(xn))

if __name__ == "__main__":
	main()