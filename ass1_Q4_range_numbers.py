#Ask the user to enter a starting number and a final number and print out each even 
#number between these two numbers

num1 = int(input('Please type the first number of the range:'))

num2 = int(input('Please type the second number:'))

if num1>num2:
    print("First number should be lesser than second number")
elif num1<num2:
    print(list(range(num1+1,num2)))
