#Write a function that asks the user for a username and password and if these are correct 
#gives the user their exam mark and a suitable message. The mark will be randomly 
#generated and correspond to a message in a list.

import random
while True:
    print ('Please enter your name?')
    name = input ()
    if name != 'Amy':
        continue #repeats code till correct name is entered
    print('Hi, Amy. What is the password')
    password = input()
    if password == 'volver':
        break #breaks continue loop
    else:
        print('Either username or password are not correct, please try again')
print('Access granted.')
number = list(range(1,101)) #between 1-100
random.shuffle(number)
result = number[:1] # [x]
print("Your Exam mark out of 100 is:")
print(result)
response = int(input(result)) #responds if pass or fail and converts string to integer
if response < 40:
    print ('Sorry, you have not passed on this attempt')
elif response >= 40:
    print ('Well done, you have passed the exam')
