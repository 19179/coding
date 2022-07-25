


def not_blank(question):
	vaid = False

	while not vaid:
		response = input(question)
		
		if response !="":
			return response
		else:
			print("sorry - this cant be blank"
					 "please enter your name")


# Main routine goes here
name = not_blank("Name: ")