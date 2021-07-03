"""
File: quadratic_solver.py
Name:Eric Cheng
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program calculates the roots of quadratic equation in one variable.
	It stores coefficients we input in a floating form,and the coefficient of x^2 cannot be 0.
	Then it would determine the states of root by discriminant which is negative, positive or 0.
	"""
	print('stanCode Quadratic Solver!')
	a = float(input('Enter a: '))
	if a == 0:  											# a is not allowed to be 0
		a = float(input('Enter a (a is not equal to 0) : '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	discriminant = b*b - 4 * a * c
	if discriminant > 0:
		x1 = (-b + math.sqrt(discriminant)) / (2 * a)  #忘了加括弧
		x2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print('Two roots: '+str(x1) + ' , ' + str(x2))
	elif discriminant == 0:
		x = - b / (2 * a) #忘了加括弧
		print('One root: '+str(x))
	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
