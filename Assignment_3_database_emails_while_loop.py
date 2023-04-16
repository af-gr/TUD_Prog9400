import re
EmailDB = [] #create an empty list to store email addresses
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
print("2. Remove existing email address\n")
choice = int(input("Enter your option: "))
if choice == 1: #I. allowing the user to enter an email address in the format firstname.secondname@domain.ie
    while True:
        newEmail = input('Please enter the email you wish to add to the database in the format firstname.secondname@domain.ie, or type ''Quit'' to exit:')
            continue
        #IV. some error checking for example checking if a particular email address they enter has an error such as has no @ sign.
        if re.match(r"[^@]+@[^@]+\.[^@]+", newEmail): # check if email is valid
            #elif email not in EmailDB: #check if email is already in the list
                EmailDB.append(newEmail)
                print(newEmail + " has been added to the email list, type 'Quit' to exit.")
        elif newEmail == 'Quit':
            break #breaks continue loop
        else:
            print('Please input in the format firstname.secondname@domain.ie')   
	
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
    
import os
# change directory
os.chdir('EmailDBFolder')
# open the file
with open('EmailDB.txt', 'r') as file:
    # do something with the file
    print(os.path.abspath(file.name)) # print the absolute path    
#change to an absolute address:
import os

# set the absolute path
path = '/Users/EmailDBFolder/EmailDB.txt'

# open the file
with open(path, 'r') as file:
    # do something with the file
    print(os.path.abspath(file.name)) # print the absolute path

#VI. using suitable string methods to separate the email addresses into first name, second name as well as the address.

newEmail = 'mickey.mouse@disney.ie'

# split the email address into parts
parts = email.split('@')
name_parts = parts[0].split('.')
first_name, last_name = name_parts[0], name_parts[1]
address = parts[1]

print(firstname) # 'mickey'
print(lastname) # 'mouse'
print(address) # 'disney.ie'

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
