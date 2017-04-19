'''
Author : Nilesh Chaturvedi
Last updated : 18th April 2017

Description : This routine uses gradient descent method to return the point of minima of a polynomial. 
'''
import math

degree = input("Highest Degree of the polynomial : ")

coefs = input("Enter the co-efficient of each term starting with highest degree first (separate them by spaces) : ").split()

descent_rate = float(input("Rate of descent : "))

starting_point = float(input("Starting point : "))

grad_coef_vector = []
permissible_error = 0.0000001
gradient = 0

x0 = starting_point
xn = 0

power = int(degree)
for x in range(power+1):
	grad_coef_vector.append(power * int(coefs[x]))
	power -= 1 

grad_coef_vector = list(reversed(grad_coef_vector))

print(grad_coef_vector)


error = float('inf')
while (error >= permissible_error):
	power = 0
	gradient = 0
	if(xn == 0):
		gradient  = grad_coef_vector[1]
	else:
		for i in grad_coef_vector[1:]:
			gradient += i * math.pow(xn, power) 
			power+=1

	# Calculate gradient	
	print("gradient %d"%gradient)
	xn = x0 - (descent_rate * gradient)
	print("xn %d"%xn)
	error = abs(xn - x0)
	print("error %d"%error)
	x0=xn


print(" Point of minima is : {}".format(xn))