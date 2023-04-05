#password program

while True:
    print('Enter your 4 digit pin:')
    pin = input()
    if pin.isdecimal():
        break
    print('Please enter numbers only.')
while True:
    print('Choose a new password (containing letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only contain letters and numbers')
        



