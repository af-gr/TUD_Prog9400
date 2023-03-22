import random

#Ask which lottery
print("I can generate numbers for the Irish Lotto or EuroMillions, which would you like? Please choose option 1 or 2")
print("1. Irish Lotto")
print("2. Euromillions")

choice = int(input("Enter your option: "))


if choice == 1:
        number = list(range(1,48))
        random.shuffle(number)
        six_number = number[:6] # [x, x, x, x, x]
        print("Your Irish Lotto numbers are")
        print(six_number)    
	
elif choice == 2:
            number = list(range(1,51))
            random.shuffle(number)
            five_number = number[:5] # [x, x, x, x, x]
            print("Your EuroMillions numbers are")
            print(five_number)
            numberst = list(range(1,13))
            random.shuffle(numberst)
            star_number = numberst[:2] # [x, x]
            print("Your Lucky Stars are")
            print(star_number)
	
else:
        print("Sorry, please enter option 1 for Irish Lotto or 2 for Euromillions, try again")




