print ('Welcome to the email database generator')
#asks the user for a password and username
myName = input('Hello, please verify your name:') 
myPass = input('Please enter your password:') 
if myName == 'Eileen':
    print ('Hello, ' + myName)
    if myPass == 'PROG9400':
        print ('Access granted')


        #If these are correct it should then print out a menu of options that the user can 
        #chose from. For example, 1 = add email address, 2 = remove email address etc. 
        #The options should include, 
        #I. allowing the user to enter an email address in the format firstname.secondname@domain.ie 
        #II. allowing the user to check an address is present and remove it if so 
        #III. allowing the user to check an address is present in the database and allowing you to add it if not.
        print('Please enter the email you wish to add to the database in the format firstname.secondname@domain.ie')
        newEmail = input()



#incorrect password entered
    else:
        print ('Sorry, thats not right, please try again')









#create an empty list of email addresses
email_list = list()

# Writing the email addresses to the file
f = open("email_database.txt", 'w')







 
 
#IV. some error checking for example checking if a particular email address they enter 
#has an error such as has no @ sign. 
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
