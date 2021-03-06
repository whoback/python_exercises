# The formulas are
# C = (F − 32) × 5 / 9
# and
# F = (C × 9 / 5) + 32
# Example Output
# Press C to convert from Fahrenheit to Celsius.
# Press F to convert from Celsius to Fahrenheit.
# Your choice: C
# Please enter the temperature in Fahrenheit: 32
# The temperature in Celsius is 0.
# Constraints
# • Ensure that you allow upper or lowercase values for C
# and F.
# • Use as few output statements as possible and avoid
# repeating output strings.
# Challenges
# • Revise the program to ensure that inputs are entered as
# numeric values. Don’t allow the user to proceed if the
# value entered is not numeric.
# • Break the program into functions that perform the
# computations.
# • Implement this program as a GUI program that automatically
# updates the values when any value changes.
# • Modify the program so it also supports the Kelvin scale.

cel_strings = ['c', 'C']
far_strings = ['f', 'F']

def conversion_choice():
	global conversion_choice
	
	while conversion_choice not in cel_strings and conversion_choice not in far_strings:
		conversion_choice = str(input('Press C to convert from Fahrenheit to Celsius. \n''Press F to convert from Celsius to Fahrenheit. \n''Your choice: '))

	return(conversion_choice)

def to_fahrenheit():
	while True:
		try:
			temp_in_celcius = int(input('Please enter the temperature in Celsius: '))
			break
		except Exception as e:
			print('You must enter the temperature as a number.')
	converted_to_fahrenheit = (temp_in_celcius * 9 / 5) + 32
	print_results('Fahrenheit', converted_to_fahrenheit)

def to_celcius():
	while True:
		try:
			temp_in_fahrenheit = int(input('Please enter the temperature in Fahrenheit: '))
			break
		except Exception as e:
			print('You must enter the temperature as a number.')
	converted_to_celcius = (temp_in_fahrenheit - 32) * 5 / 9
	print_results('Celcius', converted_to_celcius)


def print_results(string, temp):
	print('The temperature in %s is:%3d degrees'%(string, temp))


def which_key(conversion_choice):
	if conversion_choice in cel_strings:
		to_celcius()
	elif conversion_choice in far_strings:
		to_fahrenheit()			




conversion_choice()

which_key(conversion_choice)





