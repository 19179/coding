# funtion goes here

def int_check(question, low_num, high_num):
 
	error = "please enter a whole number between {} " 
	"and {}".format(low_num, high_num)
	
	valid = False
	while not valid:

		# ask user for number and check it is valid
		try:
			response = int(input(question))
			return response

			if low_num < response < high_num:
				print(error)
			else:
				return response

		# if an integer is not entered, displayed an error
		except ValueError:
			print(error)



# main routine goes here 
age = int_check("Age: ", 12, 130)