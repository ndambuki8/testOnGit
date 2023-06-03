#Factorial of a number using a for loop

num = 6

factorial = 1

if num < 0:
    print("Fact of a num less than 0 haiko")
elif num == 0:
    print("The fact of ", num, " is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("The factorial of ", num, " is ", factorial)