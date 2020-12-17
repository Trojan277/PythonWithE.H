def calc(a,b,ops):

	if ops not in "^+-*/":
		return "Please enter one of the following actions: ^+-*/"

	if ops == "^":
		return (str(a)+" ^ "+str(b) + " = " + str(a**b))
	if ops == "+":
		return (str(a)+" + "+str(b) + " = " + str(a+b))
	if ops == "-":
		return (str(a)+" - "+str(b) + " = " + str(a-b))
	if ops == "*":
		return (str(a)+" * "+str(b) + " = " + str(a*b))
	if ops == "/":
		return (str(a)+" / "+str(b) + " = " + str(a/b))

while True:
	try:
		a = int(input("Enter the first number: "))
		b = int(input("Enter the second number: "))
		ops= input("Choose your action: ^+-*/")
		print(calc(a,b,ops))
	except:
		print("Please enter the numbers properly")
