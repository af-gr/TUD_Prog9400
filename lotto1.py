import random
number = list(range(1,51))
random.shuffle(number)
five_number = number[:5]
print(five_number)     # [44, 23, 34, 38, 3]
