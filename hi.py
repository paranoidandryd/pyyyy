def helloWorld():
    print("Hi")
    myName = input("What is your name? (Enter in quotation marks) ")

    if(myName == "Kate"):
        print("u r so kewl")
    elif(myName == "Patrick"):
        print("hay babe")
    else:
		print("I don't know you.")

helloWorld()

def goodbyeWorld():
	myVar = input("Type a number: ")
	
	if(myVar < 0): 
		print("u seem v creative")
	elif(myVar == 0): 
		print("so deep")
	elif(myVar > 0):
		print("thx")

goodbyeWorld()
		
def main():
	helloWorld()
	goodbyeWorld()

	main()


