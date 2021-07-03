"""
File: weather_master.py
Name:Eric Cheng
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
CONSTANT = -100


def main():
	"""
	This program provides the function to show the highest, lowest ,average temperature
	and number of cold days.Initially,we input the first data of temperature,then if it is valid
	(data is not equal to the value of CONSTANT), we can continue to input next temperature.
	"""
	print('stanCode "Weather Master 4.0"!')
	tem = int(input('Next temperature: (or ' + str(CONSTANT) + ' to quit)? '))
	if tem == CONSTANT:
		print('No temperatures were entered.')
	else:  # Edge case
		maximum = tem
		minimum = tem
		sum_ = tem
		n = 1
		avg = sum_ / n
		alert = 0  						# Initialize the value
		if tem < 16:
			alert = 1
		while True:  					# Loop for entering following data
			tem = int(input('Next temperature: (or ' + str(CONSTANT) + ' to quit)? '))
			if tem == CONSTANT:
				break
			if tem > maximum:
				maximum = tem
			if tem < minimum:
				minimum = tem
			if tem < 16:
				alert += 1
			sum_ = sum_ + tem
			n += 1
			avg = sum_ / n
		print('Highest Temperature = ' + str(maximum))
		print('Lowest Temperature = ' + str(minimum))
		print('Average = ' + str(avg))
		print(str(alert) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
