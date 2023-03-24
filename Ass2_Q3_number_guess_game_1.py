import random as r

print('Number Guessing Game')

gs_number = r.randint(1,101) # number between 1-100
user_guess = int(input('\nYou have 7 guesses to guess any number between 1 and 100, enter your guess: '))
turn = 1

while True:
        
    if gs_number == user_guess:
        print(f'Congratulations you guessed the number in {turn} attempts.')
        break
    #elif turn == 4:
        #print('Do you want a clue? (Y/N)')
            #if ('N' in clue):
        #continue
            #clue = input
            #elif 'Y' in clue:
        break
    elif turn == 7:
        print(f'Sorry You didn\'t guess the number. The number is {gs_number}')
        break
    else:
        if gs_number > user_guess:
            print('Too Low')
        else:
            print('Too High')

        print(f'You have (7-{turn}) guesses left.')
        turn += 1
        user_guess = int(input('Guess again : '))

  
