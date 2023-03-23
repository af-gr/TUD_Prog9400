#Program for printing multiplication table up to 20 times table
print('This tool generates a multiplication table for numbers between 1 and 20')
n=int(input('Please enter a positive integer between 1 and 20: '))
if 20 > n and n > 0: #only allows numbers between 1 and 20
    print("-----------------------------------------") #header
    print("Multiplication Table for Multiples of",n)
    print("-----------------------------------------")
    for row in range(1,n+1):
        for col in range(1,n+1):
            print("|",row*col, end="\t")
        print()
else: print('Sorry I cannot calculate numbers over 20, please try again') #exception statement


