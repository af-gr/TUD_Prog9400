#Ask what month and year
print("Please enter numerically the month you would like to know the number of days from, e.g. for May, type 5?")
month = int(input())
print("Of which year please?")
year = int(input())
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
	print("There are 31 days")
#feb leap year
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))):	
	print("This is a leap year, therefore there are 29 days")
#feb non leap year
elif(month == 2):
	print("There are 28 days")
else:
	print("There are 30 days")
