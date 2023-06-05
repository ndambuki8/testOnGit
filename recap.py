#Factorial of a number using recursion

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

#Change the value for a different result
num = 6

result = factorial(num)

print("The factorial of", num, "is",result)