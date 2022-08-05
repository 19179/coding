# import statements
import number_checker

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
			
# start of loop 

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5 

while name != "xxx" and count < MAX_TICKETS:
	
	# tells user how many seats are left
	if count < 4:
		print("You have {} seats "
			"left".format(MAX_TICKETS - count))
	
		# Warns user that only one seat is left!
	else:
		print("*** There is ONE seat left!! ***")
	
	# Gets details...
	name = input("Name: ")
	count += 1


if count == MAX_TICKETS:
	print("You have sold all the avaiable tickets!")
else:
	print("You have sold {} tickets. \n"
			 "There are {} places still available"
			 .format (count, MAX_TICKETS - count))
	# Get name (can't be blank)
	name = not_blank("Name: ")
	# Get age (between 12 and 130)

	# Calculate ticket price

	# Loop to ask for snacks

	# Calculate snack price

	# ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file