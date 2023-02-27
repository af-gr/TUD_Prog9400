# This program asks the user for a number then gives the factorial
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

inputfact = int(input("Enter a number and I will give you the factorial (a factorial of a number such as 5 is equal to 5 * 4 * 3 * 2 * 1 = 120.): "))
fact = factorial(inputfact)
print(f"The factorial of {inputfact} is {fact}")
