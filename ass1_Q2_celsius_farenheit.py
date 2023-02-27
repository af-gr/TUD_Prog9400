#Formula to define conversion
def cel2far(a):
	return (9/5)*a + 32
def far2cel(a):
	return (a-32) * (5/9)

#Ask if the user is converting celsius to farenheit or viceversa
print("I can convert from celsius to farenheit or viceversa, which would you like? Please choose option 1 or 2")
print("1. From Celsius to Farenheit [C to F]")
print("2. From Farenheit to Celsius [F to C]")

choice = int(input("Enter your option: "))

#Ask for a number
a = float(input("Please enter the number you would like to convert: "))

#Conversion
if choice == 1:
	c = cel2far(a)
	print("{0}C converted is equal to {1}F" .format(a, c))
elif choice == 2:
	f = far2cel(a)
	print("{0}F converted is equal to {1}C" .format(a, f))
	
#else:
        #print("Sorry, I can only convert celsius and farenheit, please try again"
