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
permessible_error = 0.0000001
gradient = 0

x0 = starting_point
xn = 0

power = int(degree)
for x in range(power+1):
	grad_coef_vector.append(power * int(coefs[x]))
	power -= 1 
print(grad_coef_vector)


error = 999999999999999
while (error >= permessible_error):
	# Calculate gradient
	power = int(degree)-1
	
	for i in grad_coef_vector:
		if(power>0):
			gradient += i * math.pow(x0, power)
		else:
			gradient += 0 
		power-=1	

	print("gradient %d"%gradient)
	xn = x0 - (descent_rate * gradient)
	print("xn %d"%xn)
	error = abs(xn - x0)
	print("error %d"%error)
	xn = 0
	x0=xn

print(" Point of minima is : {}".format(xn))