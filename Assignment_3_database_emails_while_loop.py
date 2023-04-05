print ('Welcome to the email database generator\n'.center(20,'*'))
#asks the user for a password and username
while True:
    myName = input('Please verify your name: ') 
    if myName != 'Eileen':
        continue #repeats code till correct name is entered
    if myName == 'Eileen':
        print ('Hello, ' + myName)
        print('What is the password?')
    myPass = input()
    if myPass == 'PROG9400':
        break #breaks continue loop   
    else:
        #wrong password
        print('That is incorrect, please try again, entries are case-sensitive')
print ('\n Access granted, please choose option 1, 2 or 3:\n')
#If these are correct it should then print out a menu of options that the user can 
#chose from. For example, 1 = add email address, 2 = remove email address etc. 
print("1. Add new email address")
print("2. Remove existing email address")
print("3. Check if email already present\n")
choice = int(input("Enter your option: "))
if choice == 1: #I. allowing the user to enter an email address in the format firstname.secondname@domain.ie
    while True:
        print('Please enter the email you wish to add to the database in the format firstname.secondname@domain.ie:')
        newEmail = input()
        #IV. some error checking for example checking if a particular email address they enter has an error such as has no @ sign.
        if newEmail.isdecimal():
            break
        print('Please input in the format firstname.secondname@domain.ie')
    while True:
        print('Choose a new password (containing letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only contain letters and numbers')

        EmailDB = open ('C:\\EmailDBFolder\\EmailDB.txt', 'w')
        EmailDB.write (newEmail'\n)

        EmailDB = open ('C:\\EmailDBFolder\\EmailDB.txt', 'w')
        content = EmailDB.read()
        EmailDB.close()
        print(content)
        

    

    #create an empty list of email addresses
    #email_list = list()

    #Writing the email addresses to the file
    #f = open("email_database.txt", 'w')             
	
elif choice == 2:  #II. allowing the user to check an address is present and remove it if so
    print("Please enter the email you wish to remove from the database in the format firstname.secondname@domain.ie")
    rmvEmail = input()

    EmailDB = open ('C:\\EmailDBFolder\\EmailDB.txt', 'w')
    content = EmailDB.read()
    EmailDB.close()
    print(content)
    
       


#incorrect email format entered
else:
    print ('Sorry, an incorrect format has been entered, please try again')



 
 
 
#V. changing the address for the text file storing the addresses to either a relative or 
#absolute address and printing this out 
#VI. using suitable string methods to separate the email addresses into first name, 
#second name as well as the address. 
#For example, if the user enters mickey.mouse@disney.ie the text file should store 
#mickey, mouse,  and mickey.mouse@disney.ie using suitable delimiters. 
#VII. Tell the user how many entries there are in the database and ask the user how many 
#names and addresses the user wants to print out and print out the first number of 
#names or, if the user choses, all the names and email addresses. 
#VIII. Print out a formatted short (one paragraph) letter to the first number of email 
#addresses that includes their name and their email address. 

#For example, 
 
#Dear Mickey Mouse, 
#   Thank for ordering the acme comedy hammer. We will be 
#emailing you shortly with the full specifications. Can you confirm that your email 
#address is mickey.mouse@disney.ie? 
 
#Kind regards 
#Eileen 
