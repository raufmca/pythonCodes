#ZeroDivisionError try Block 

x = int ( input (" Enter the first number = "))

y = int ( input (" Enter the second number = "))

try:
	z = x/y
except ZeroDivisionError:
	print(" Cannot divide by zero ZeroDivisionError !!")
finally:
	print( " Close the program ")
