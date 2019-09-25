# print square of integers

def ask():

	while True:
		try:

			num = int ( input ( " Enter the number = "))

		except:
			print( " Please try ith number \n")
			continue
		else:
			print( num **2)
			print(" End of function")
			break

if __name__ == '__main__':
	Ask()