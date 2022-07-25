# import statements
import ticket_loop_v1
# funtions go here


# checks that ticket name is not blank
def not_blank(question):
	vaid = False

	while not vaid:
		response = input(question)
		
		if response !="":
			return response
		else:
			print("sorry - this cant be blank, "
					 "please enter your name")

# ********** Main Routine **********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details 

	# Get name (can't be blank)
	name = not_blank("Name: ")
	# Get age (between 12 and 130)

	# Calculate ticket price

	# Loop to ask for snacks

	# Calculate snack price

	# ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file