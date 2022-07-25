


def not_blank(question, error_message):
	vaid = False

	while not vaid:
		response = input(question)
		
		if response !="":
			return response
		else:
			print(error_message)


# Main routine goes here
name = not_blank("Name: ", 
	"sorry this cant be blank,"
	"please enter your name")