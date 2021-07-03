"""
File: rocket.py
Name: Eric Cheng
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	There are 4 different functions : head(),belt(),upper(),lower(). They would print the
	components of a rocket,thus we can draw a rocket by assembling them. This rocket is
	stretchable by changing the constant: SIZE.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	This function prints shape of rocket head
	According to observe the coordinates of characters,we can find their regularity.
	The number of row is SIZE ,column is twice SIZE.
	"""
	for i in range(SIZE):
		print(' ', end='')  # match the shape out of belt()
		for j in range(2 * SIZE):
			if i+j < SIZE - 1:
				print(' ', end='')
			elif j <= SIZE - 1:
				print('/', end='')
			elif j-i <= SIZE:
				print('\\', end='')
			else:
				print(' ', end='')
		print('')


def belt():
	"""
	This function prints the belt of rocket
	"""
	for i in range(2 * SIZE + 2):
		if i == 0:
			print('+', end='')
		elif i < 2 * SIZE + 1:
			print('=', end='')
		else:
			print('+', end='')
	print('')


def upper():
	"""
	This function prints the upper part of rocket.
	"""
	for i in range(SIZE):
		a = 0
		for j in range(2 * SIZE + 2):
			if j == 0:
				print('|', end='')
			elif j < SIZE-i:
				print('.', end='')
			elif j < SIZE + i + 2 and a == 0:
				print('/', end='')
				a += 1
			elif a == 1:
				print('\\', end='')
				a = 0
			elif SIZE + i + 2 <= j < 2 * SIZE + 1:
				print('.', end='')
			else:
				print('|', end='')
		print('')


def lower():
	"""
	This function prints the lower part of rocket.
	"""
	for i in range(SIZE):
		a = 0
		for j in range(2 * SIZE + 2):
			if j == 0:
				print('|', end='')
			elif j <= i:
				print('.', end='')
			elif i + j <= 2 * SIZE and a == 0:
				print('\\', end='')
				a += 1
			elif a == 1:
				print('/', end='')
				a = 0
			elif j <= 2 * SIZE:
				print('.', end='')
			else:
				print('|', end='')
		print()


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()