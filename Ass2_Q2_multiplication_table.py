print('This tool generates a multiplication table for numbers between 1 and 20')
num, b, c, count = int(input('Please enter a number:')), '  ', '   ', 0
for i in range(1, num+1):
    if i > 9:
        b = b + str(i) + '   '
        c = c + str(i) + '|'
    else:
        b = b + str(i) + '    '
        c = c + str(i) + ' |'
    for a in range(1, num+1):
        d = str(a*i)
        for letter in d:
            count += 1
        c = c + str(a*i) + ' '*(5-count)
        count = 0
    c = c + '\n   '
print((' ')*4 + b)
print((' ')*6 + ('-'+ '    ')*num)
print(c)

#else: print('Sorry I cannot calculate numbers over 20, please try again')

#n=int(input('Please enter a positive integer between 1 and 15: '))
#for row in range(1,n+1):
    #for col in range(1,n+1):
        #print(row*col, end="\t")
    #print()
